_c='portTrunkMember'
_b='portTrunkId'
_a='vlanPortVlanId'
_Z='vlanPortPortId'
_Y='createAndGo'
_X='vlanId'
_W='configIpFilterIpAddress'
_V='configDiffServDSCP'
_U='normal'
_T='rate1Gig'
_S='rate100Meg'
_R='rate10Meg'
_Q='full-duplex'
_P='half-duplex'
_O='configPort'
_N='hostIndex'
_M='commIndex'
_L='destroy'
_K='active'
_J='write-only'
_I='noop'
_H='POWERCONNECT3048-MIB'
_G='DisplayString'
_F='read-only'
_E='enabled'
_D='disabled'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class OwnerString(DisplayString):0
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,674))
_DellLan_ObjectIdentity=ObjectIdentity
dellLan=_DellLan_ObjectIdentity((1,3,6,1,4,1,674,10895))
_Powerconnect3048_ObjectIdentity=ObjectIdentity
powerconnect3048=_Powerconnect3048_ObjectIdentity((1,3,6,1,4,1,674,10895,5))
_DellCommGroup_ObjectIdentity=ObjectIdentity
dellCommGroup=_DellCommGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5,1))
_CommTable_Object=MibTable
commTable=_CommTable_Object((1,3,6,1,4,1,674,10895,5,1,1))
if mibBuilder.loadTexts:commTable.setStatus(_A)
_CommEntry_Object=MibTableRow
commEntry=_CommEntry_Object((1,3,6,1,4,1,674,10895,5,1,1,1))
commEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:commEntry.setStatus(_A)
class _CommIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CommIndex_Type.__name__=_C
_CommIndex_Object=MibTableColumn
commIndex=_CommIndex_Object((1,3,6,1,4,1,674,10895,5,1,1,1,1),_CommIndex_Type())
commIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:commIndex.setStatus(_A)
class _CommName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CommName_Type.__name__=_G
_CommName_Object=MibTableColumn
commName=_CommName_Object((1,3,6,1,4,1,674,10895,5,1,1,1,2),_CommName_Type())
commName.setMaxAccess(_B)
if mibBuilder.loadTexts:commName.setStatus(_A)
class _CommGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_CommGet_Type.__name__=_C
_CommGet_Object=MibTableColumn
commGet=_CommGet_Object((1,3,6,1,4,1,674,10895,5,1,1,1,3),_CommGet_Type())
commGet.setMaxAccess(_B)
if mibBuilder.loadTexts:commGet.setStatus(_A)
class _CommSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_CommSet_Type.__name__=_C
_CommSet_Object=MibTableColumn
commSet=_CommSet_Object((1,3,6,1,4,1,674,10895,5,1,1,1,4),_CommSet_Type())
commSet.setMaxAccess(_B)
if mibBuilder.loadTexts:commSet.setStatus(_A)
class _CommTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_CommTrap_Type.__name__=_C
_CommTrap_Object=MibTableColumn
commTrap=_CommTrap_Object((1,3,6,1,4,1,674,10895,5,1,1,1,5),_CommTrap_Type())
commTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrap.setStatus(_A)
class _CommStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CommStatus_Type.__name__=_C
_CommStatus_Object=MibTableColumn
commStatus=_CommStatus_Object((1,3,6,1,4,1,674,10895,5,1,1,1,6),_CommStatus_Type())
commStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commStatus.setStatus(_A)
_DellHostGroup_ObjectIdentity=ObjectIdentity
dellHostGroup=_DellHostGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5,2))
_HostTable_Object=MibTable
hostTable=_HostTable_Object((1,3,6,1,4,1,674,10895,5,2,1))
if mibBuilder.loadTexts:hostTable.setStatus(_A)
_HostEntry_Object=MibTableRow
hostEntry=_HostEntry_Object((1,3,6,1,4,1,674,10895,5,2,1,1))
hostEntry.setIndexNames((0,_H,_N))
if mibBuilder.loadTexts:hostEntry.setStatus(_A)
class _HostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HostIndex_Type.__name__=_C
_HostIndex_Object=MibTableColumn
hostIndex=_HostIndex_Object((1,3,6,1,4,1,674,10895,5,2,1,1,1),_HostIndex_Type())
hostIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hostIndex.setStatus(_A)
class _HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HostName_Type.__name__=_G
_HostName_Object=MibTableColumn
hostName=_HostName_Object((1,3,6,1,4,1,674,10895,5,2,1,1,2),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
_HostIP_Type=IpAddress
_HostIP_Object=MibTableColumn
hostIP=_HostIP_Object((1,3,6,1,4,1,674,10895,5,2,1,1,3),_HostIP_Type())
hostIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIP.setStatus(_A)
class _HostComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HostComm_Type.__name__=_G
_HostComm_Object=MibTableColumn
hostComm=_HostComm_Object((1,3,6,1,4,1,674,10895,5,2,1,1,4),_HostComm_Type())
hostComm.setMaxAccess(_B)
if mibBuilder.loadTexts:hostComm.setStatus(_A)
class _HostStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_HostStatus_Type.__name__=_C
_HostStatus_Object=MibTableColumn
hostStatus=_HostStatus_Object((1,3,6,1,4,1,674,10895,5,2,1,1,5),_HostStatus_Type())
hostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hostStatus.setStatus(_A)
class _HostAuthorization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HostAuthorization_Type.__name__=_C
_HostAuthorization_Object=MibScalar
hostAuthorization=_HostAuthorization_Object((1,3,6,1,4,1,674,10895,5,2,2),_HostAuthorization_Type())
hostAuthorization.setMaxAccess(_B)
if mibBuilder.loadTexts:hostAuthorization.setStatus(_A)
_DellMiscGroup_ObjectIdentity=ObjectIdentity
dellMiscGroup=_DellMiscGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5,3))
_MiscBaud_Type=Integer32
_MiscBaud_Object=MibScalar
miscBaud=_MiscBaud_Object((1,3,6,1,4,1,674,10895,5,3,1),_MiscBaud_Type())
miscBaud.setMaxAccess(_F)
if mibBuilder.loadTexts:miscBaud.setStatus(_A)
class _MiscReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_I,2)))
_MiscReset_Type.__name__=_C
_MiscReset_Object=MibScalar
miscReset=_MiscReset_Object((1,3,6,1,4,1,674,10895,5,3,2),_MiscReset_Type())
miscReset.setMaxAccess(_B)
if mibBuilder.loadTexts:miscReset.setStatus(_A)
class _MiscStatisticsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_I,2)))
_MiscStatisticsReset_Type.__name__=_C
_MiscStatisticsReset_Object=MibScalar
miscStatisticsReset=_MiscStatisticsReset_Object((1,3,6,1,4,1,674,10895,5,3,3),_MiscStatisticsReset_Type())
miscStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:miscStatisticsReset.setStatus(_A)
class _MiscSwitchOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('unknown',2),('ok',3),('noncritical',4),('critical',5),('nonrecoverable',6)))
_MiscSwitchOperState_Type.__name__=_C
_MiscSwitchOperState_Object=MibScalar
miscSwitchOperState=_MiscSwitchOperState_Object((1,3,6,1,4,1,674,10895,5,3,4),_MiscSwitchOperState_Type())
miscSwitchOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:miscSwitchOperState.setStatus('current')
_DellSpanGroup_ObjectIdentity=ObjectIdentity
dellSpanGroup=_DellSpanGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5,4))
class _SpanOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_SpanOnOff_Type.__name__=_C
_SpanOnOff_Object=MibScalar
spanOnOff=_SpanOnOff_Object((1,3,6,1,4,1,674,10895,5,4,1),_SpanOnOff_Type())
spanOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:spanOnOff.setStatus(_A)
_DellConfigGroup_ObjectIdentity=ObjectIdentity
dellConfigGroup=_DellConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5,11))
class _ConfigVerSwPrimary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ConfigVerSwPrimary_Type.__name__=_G
_ConfigVerSwPrimary_Object=MibScalar
configVerSwPrimary=_ConfigVerSwPrimary_Object((1,3,6,1,4,1,674,10895,5,11,1),_ConfigVerSwPrimary_Type())
configVerSwPrimary.setMaxAccess(_F)
if mibBuilder.loadTexts:configVerSwPrimary.setStatus(_A)
class _ConfigVerHwChipSet_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ConfigVerHwChipSet_Type.__name__=_G
_ConfigVerHwChipSet_Object=MibScalar
configVerHwChipSet=_ConfigVerHwChipSet_Object((1,3,6,1,4,1,674,10895,5,11,2),_ConfigVerHwChipSet_Type())
configVerHwChipSet.setMaxAccess(_F)
if mibBuilder.loadTexts:configVerHwChipSet.setStatus(_A)
class _ConfigBootMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('flash',1),('net',2)))
_ConfigBootMode_Type.__name__=_C
_ConfigBootMode_Object=MibScalar
configBootMode=_ConfigBootMode_Object((1,3,6,1,4,1,674,10895,5,11,3),_ConfigBootMode_Type())
configBootMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configBootMode.setStatus(_A)
_ConfigBootFtpServerIp_Type=IpAddress
_ConfigBootFtpServerIp_Object=MibScalar
configBootFtpServerIp=_ConfigBootFtpServerIp_Object((1,3,6,1,4,1,674,10895,5,11,4),_ConfigBootFtpServerIp_Type())
configBootFtpServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:configBootFtpServerIp.setStatus(_A)
class _ConfigBootImageFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ConfigBootImageFileName_Type.__name__=_G
_ConfigBootImageFileName_Object=MibScalar
configBootImageFileName=_ConfigBootImageFileName_Object((1,3,6,1,4,1,674,10895,5,11,5),_ConfigBootImageFileName_Type())
configBootImageFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:configBootImageFileName.setStatus(_A)
_ConfigPortTable_Object=MibTable
configPortTable=_ConfigPortTable_Object((1,3,6,1,4,1,674,10895,5,11,6))
if mibBuilder.loadTexts:configPortTable.setStatus(_A)
_ConfigPortEntry_Object=MibTableRow
configPortEntry=_ConfigPortEntry_Object((1,3,6,1,4,1,674,10895,5,11,6,1))
configPortEntry.setIndexNames((0,_H,_O))
if mibBuilder.loadTexts:configPortEntry.setStatus(_A)
_ConfigPort_Type=Integer32
_ConfigPort_Object=MibTableColumn
configPort=_ConfigPort_Object((1,3,6,1,4,1,674,10895,5,11,6,1,1),_ConfigPort_Type())
configPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configPort.setStatus(_A)
class _ConfigPortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ConfigPortDuplex_Type.__name__=_C
_ConfigPortDuplex_Object=MibTableColumn
configPortDuplex=_ConfigPortDuplex_Object((1,3,6,1,4,1,674,10895,5,11,6,1,3),_ConfigPortDuplex_Type())
configPortDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortDuplex.setStatus(_A)
class _ConfigPortRuntFilt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigPortRuntFilt_Type.__name__=_C
_ConfigPortRuntFilt_Object=MibTableColumn
configPortRuntFilt=_ConfigPortRuntFilt_Object((1,3,6,1,4,1,674,10895,5,11,6,1,4),_ConfigPortRuntFilt_Type())
configPortRuntFilt.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortRuntFilt.setStatus(_A)
class _ConfigPortSrcSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigPortSrcSecurity_Type.__name__=_C
_ConfigPortSrcSecurity_Object=MibTableColumn
configPortSrcSecurity=_ConfigPortSrcSecurity_Object((1,3,6,1,4,1,674,10895,5,11,6,1,5),_ConfigPortSrcSecurity_Type())
configPortSrcSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortSrcSecurity.setStatus(_A)
class _ConfigPortDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,4)))
_ConfigPortDataRate_Type.__name__=_C
_ConfigPortDataRate_Object=MibTableColumn
configPortDataRate=_ConfigPortDataRate_Object((1,3,6,1,4,1,674,10895,5,11,6,1,6),_ConfigPortDataRate_Type())
configPortDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortDataRate.setStatus(_A)
class _ConfigForwardingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('store-and-forward',1),('cut-through',2)))
_ConfigForwardingMode_Type.__name__=_C
_ConfigForwardingMode_Object=MibTableColumn
configForwardingMode=_ConfigForwardingMode_Object((1,3,6,1,4,1,674,10895,5,11,6,1,7),_ConfigForwardingMode_Type())
configForwardingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configForwardingMode.setStatus(_A)
class _ConfigPortDuplexOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ConfigPortDuplexOper_Type.__name__=_C
_ConfigPortDuplexOper_Object=MibTableColumn
configPortDuplexOper=_ConfigPortDuplexOper_Object((1,3,6,1,4,1,674,10895,5,11,6,1,8),_ConfigPortDuplexOper_Type())
configPortDuplexOper.setMaxAccess(_F)
if mibBuilder.loadTexts:configPortDuplexOper.setStatus(_A)
class _ConfigPortDataRateOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,4)))
_ConfigPortDataRateOper_Type.__name__=_C
_ConfigPortDataRateOper_Object=MibTableColumn
configPortDataRateOper=_ConfigPortDataRateOper_Object((1,3,6,1,4,1,674,10895,5,11,6,1,9),_ConfigPortDataRateOper_Type())
configPortDataRateOper.setMaxAccess(_F)
if mibBuilder.loadTexts:configPortDataRateOper.setStatus(_A)
class _ConfigPortStateOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('blocking',2),('listening',3),('learning',4),('forwarding',5)))
_ConfigPortStateOper_Type.__name__=_C
_ConfigPortStateOper_Object=MibTableColumn
configPortStateOper=_ConfigPortStateOper_Object((1,3,6,1,4,1,674,10895,5,11,6,1,10),_ConfigPortStateOper_Type())
configPortStateOper.setMaxAccess(_F)
if mibBuilder.loadTexts:configPortStateOper.setStatus(_A)
class _ConfigPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigPortFlowControl_Type.__name__=_C
_ConfigPortFlowControl_Object=MibTableColumn
configPortFlowControl=_ConfigPortFlowControl_Object((1,3,6,1,4,1,674,10895,5,11,6,1,11),_ConfigPortFlowControl_Type())
configPortFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortFlowControl.setStatus(_A)
class _ConfigPortDefaultVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ConfigPortDefaultVlanId_Type.__name__=_C
_ConfigPortDefaultVlanId_Object=MibTableColumn
configPortDefaultVlanId=_ConfigPortDefaultVlanId_Object((1,3,6,1,4,1,674,10895,5,11,6,1,12),_ConfigPortDefaultVlanId_Type())
configPortDefaultVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortDefaultVlanId.setStatus(_A)
class _ConfigPortComments_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ConfigPortComments_Type.__name__=_G
_ConfigPortComments_Object=MibTableColumn
configPortComments=_ConfigPortComments_Object((1,3,6,1,4,1,674,10895,5,11,6,1,13),_ConfigPortComments_Type())
configPortComments.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortComments.setStatus(_A)
class _ConfigPortAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigPortAutoNegotiation_Type.__name__=_C
_ConfigPortAutoNegotiation_Object=MibTableColumn
configPortAutoNegotiation=_ConfigPortAutoNegotiation_Object((1,3,6,1,4,1,674,10895,5,11,6,1,14),_ConfigPortAutoNegotiation_Type())
configPortAutoNegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortAutoNegotiation.setStatus(_A)
class _ConfigPortHOLBlocking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigPortHOLBlocking_Type.__name__=_C
_ConfigPortHOLBlocking_Object=MibTableColumn
configPortHOLBlocking=_ConfigPortHOLBlocking_Object((1,3,6,1,4,1,674,10895,5,11,6,1,15),_ConfigPortHOLBlocking_Type())
configPortHOLBlocking.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortHOLBlocking.setStatus(_A)
class _ConfigPortFlowControlOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigPortFlowControlOper_Type.__name__=_C
_ConfigPortFlowControlOper_Object=MibTableColumn
configPortFlowControlOper=_ConfigPortFlowControlOper_Object((1,3,6,1,4,1,674,10895,5,11,6,1,16),_ConfigPortFlowControlOper_Type())
configPortFlowControlOper.setMaxAccess(_F)
if mibBuilder.loadTexts:configPortFlowControlOper.setStatus(_A)
class _ConfigPortGBIC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_ConfigPortGBIC_Type.__name__=_C
_ConfigPortGBIC_Object=MibTableColumn
configPortGBIC=_ConfigPortGBIC_Object((1,3,6,1,4,1,674,10895,5,11,6,1,17),_ConfigPortGBIC_Type())
configPortGBIC.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortGBIC.setStatus(_A)
class _ConfigPortFastLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ConfigPortFastLink_Type.__name__=_C
_ConfigPortFastLink_Object=MibTableColumn
configPortFastLink=_ConfigPortFastLink_Object((1,3,6,1,4,1,674,10895,5,11,6,1,18),_ConfigPortFastLink_Type())
configPortFastLink.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortFastLink.setStatus(_A)
class _ConfigPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('high',2)))
_ConfigPortPriority_Type.__name__=_C
_ConfigPortPriority_Object=MibTableColumn
configPortPriority=_ConfigPortPriority_Object((1,3,6,1,4,1,674,10895,5,11,6,1,19),_ConfigPortPriority_Type())
configPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortPriority.setStatus(_A)
class _ConfigRmonOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigRmonOnOff_Type.__name__=_C
_ConfigRmonOnOff_Object=MibScalar
configRmonOnOff=_ConfigRmonOnOff_Object((1,3,6,1,4,1,674,10895,5,11,7),_ConfigRmonOnOff_Type())
configRmonOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:configRmonOnOff.setStatus(_A)
class _ConfigMirroringOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigMirroringOnOff_Type.__name__=_C
_ConfigMirroringOnOff_Object=MibScalar
configMirroringOnOff=_ConfigMirroringOnOff_Object((1,3,6,1,4,1,674,10895,5,11,8),_ConfigMirroringOnOff_Type())
configMirroringOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirroringOnOff.setStatus(_A)
_ConfigMirrorSrc_Type=Integer32
_ConfigMirrorSrc_Object=MibScalar
configMirrorSrc=_ConfigMirrorSrc_Object((1,3,6,1,4,1,674,10895,5,11,9),_ConfigMirrorSrc_Type())
configMirrorSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorSrc.setStatus(_A)
_ConfigMirrorMon_Type=Integer32
_ConfigMirrorMon_Object=MibScalar
configMirrorMon=_ConfigMirrorMon_Object((1,3,6,1,4,1,674,10895,5,11,10),_ConfigMirrorMon_Type())
configMirrorMon.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorMon.setStatus(_A)
class _ConfigIpAssignmentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('bootP',2),('dhcp',3)))
_ConfigIpAssignmentMode_Type.__name__=_C
_ConfigIpAssignmentMode_Object=MibScalar
configIpAssignmentMode=_ConfigIpAssignmentMode_Object((1,3,6,1,4,1,674,10895,5,11,12),_ConfigIpAssignmentMode_Type())
configIpAssignmentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpAssignmentMode.setStatus(_A)
_ConfigPhysAddress_Type=MacAddress
_ConfigPhysAddress_Object=MibScalar
configPhysAddress=_ConfigPhysAddress_Object((1,3,6,1,4,1,674,10895,5,11,13),_ConfigPhysAddress_Type())
configPhysAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:configPhysAddress.setStatus(_A)
class _ConfigPasswordUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ConfigPasswordUser_Type.__name__=_G
_ConfigPasswordUser_Object=MibScalar
configPasswordUser=_ConfigPasswordUser_Object((1,3,6,1,4,1,674,10895,5,11,14),_ConfigPasswordUser_Type())
configPasswordUser.setMaxAccess(_J)
if mibBuilder.loadTexts:configPasswordUser.setStatus(_A)
class _ConfigPasswordAdmin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ConfigPasswordAdmin_Type.__name__=_G
_ConfigPasswordAdmin_Object=MibScalar
configPasswordAdmin=_ConfigPasswordAdmin_Object((1,3,6,1,4,1,674,10895,5,11,15),_ConfigPasswordAdmin_Type())
configPasswordAdmin.setMaxAccess(_J)
if mibBuilder.loadTexts:configPasswordAdmin.setStatus(_A)
_ConfigIpAddress_Type=IpAddress
_ConfigIpAddress_Object=MibScalar
configIpAddress=_ConfigIpAddress_Object((1,3,6,1,4,1,674,10895,5,11,16),_ConfigIpAddress_Type())
configIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpAddress.setStatus(_A)
_ConfigNetMask_Type=IpAddress
_ConfigNetMask_Object=MibScalar
configNetMask=_ConfigNetMask_Object((1,3,6,1,4,1,674,10895,5,11,17),_ConfigNetMask_Type())
configNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:configNetMask.setStatus(_A)
_ConfigGateway_Type=IpAddress
_ConfigGateway_Object=MibScalar
configGateway=_ConfigGateway_Object((1,3,6,1,4,1,674,10895,5,11,18),_ConfigGateway_Type())
configGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:configGateway.setStatus(_A)
class _ConfigSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('save',1),(_I,2)))
_ConfigSave_Type.__name__=_C
_ConfigSave_Object=MibScalar
configSave=_ConfigSave_Object((1,3,6,1,4,1,674,10895,5,11,19),_ConfigSave_Type())
configSave.setMaxAccess(_B)
if mibBuilder.loadTexts:configSave.setStatus(_A)
class _ConfigVerifyPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ConfigVerifyPassword_Type.__name__=_G
_ConfigVerifyPassword_Object=MibScalar
configVerifyPassword=_ConfigVerifyPassword_Object((1,3,6,1,4,1,674,10895,5,11,20),_ConfigVerifyPassword_Type())
configVerifyPassword.setMaxAccess(_J)
if mibBuilder.loadTexts:configVerifyPassword.setStatus(_A)
class _ConfigVerBootRomImage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ConfigVerBootRomImage_Type.__name__=_G
_ConfigVerBootRomImage_Object=MibScalar
configVerBootRomImage=_ConfigVerBootRomImage_Object((1,3,6,1,4,1,674,10895,5,11,21),_ConfigVerBootRomImage_Type())
configVerBootRomImage.setMaxAccess(_F)
if mibBuilder.loadTexts:configVerBootRomImage.setStatus(_A)
class _ConfigRestoreDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restore',1),(_I,2)))
_ConfigRestoreDefaults_Type.__name__=_C
_ConfigRestoreDefaults_Object=MibScalar
configRestoreDefaults=_ConfigRestoreDefaults_Object((1,3,6,1,4,1,674,10895,5,11,22),_ConfigRestoreDefaults_Type())
configRestoreDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:configRestoreDefaults.setStatus(_A)
class _ConfigIGMPOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigIGMPOnOff_Type.__name__=_C
_ConfigIGMPOnOff_Object=MibScalar
configIGMPOnOff=_ConfigIGMPOnOff_Object((1,3,6,1,4,1,674,10895,5,11,23),_ConfigIGMPOnOff_Type())
configIGMPOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:configIGMPOnOff.setStatus(_A)
class _ConfigWebOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigWebOnOff_Type.__name__=_C
_ConfigWebOnOff_Object=MibScalar
configWebOnOff=_ConfigWebOnOff_Object((1,3,6,1,4,1,674,10895,5,11,24),_ConfigWebOnOff_Type())
configWebOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:configWebOnOff.setStatus(_A)
class _ConfigHighPriorityOptimization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigHighPriorityOptimization_Type.__name__=_C
_ConfigHighPriorityOptimization_Object=MibScalar
configHighPriorityOptimization=_ConfigHighPriorityOptimization_Object((1,3,6,1,4,1,674,10895,5,11,25),_ConfigHighPriorityOptimization_Type())
configHighPriorityOptimization.setMaxAccess(_B)
if mibBuilder.loadTexts:configHighPriorityOptimization.setStatus(_A)
class _ConfigDynamicAddressLearning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigDynamicAddressLearning_Type.__name__=_C
_ConfigDynamicAddressLearning_Object=MibScalar
configDynamicAddressLearning=_ConfigDynamicAddressLearning_Object((1,3,6,1,4,1,674,10895,5,11,26),_ConfigDynamicAddressLearning_Type())
configDynamicAddressLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:configDynamicAddressLearning.setStatus(_A)
class _ConfigUserAuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),('localThenRemote',2),('remoteThenLocal',3),('remote',4)))
_ConfigUserAuthenticationMode_Type.__name__=_C
_ConfigUserAuthenticationMode_Object=MibScalar
configUserAuthenticationMode=_ConfigUserAuthenticationMode_Object((1,3,6,1,4,1,674,10895,5,11,27),_ConfigUserAuthenticationMode_Type())
configUserAuthenticationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configUserAuthenticationMode.setStatus(_A)
_ConfigRadiusServerIpAddress_Type=IpAddress
_ConfigRadiusServerIpAddress_Object=MibScalar
configRadiusServerIpAddress=_ConfigRadiusServerIpAddress_Object((1,3,6,1,4,1,674,10895,5,11,28),_ConfigRadiusServerIpAddress_Type())
configRadiusServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:configRadiusServerIpAddress.setStatus(_A)
class _ConfigRadiusSharedSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ConfigRadiusSharedSecret_Type.__name__=_G
_ConfigRadiusSharedSecret_Object=MibScalar
configRadiusSharedSecret=_ConfigRadiusSharedSecret_Object((1,3,6,1,4,1,674,10895,5,11,29),_ConfigRadiusSharedSecret_Type())
configRadiusSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:configRadiusSharedSecret.setStatus(_A)
class _ConfigTelnetConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigTelnetConsole_Type.__name__=_C
_ConfigTelnetConsole_Object=MibScalar
configTelnetConsole=_ConfigTelnetConsole_Object((1,3,6,1,4,1,674,10895,5,11,30),_ConfigTelnetConsole_Type())
configTelnetConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:configTelnetConsole.setStatus(_A)
_ConfigDiffServTable_Object=MibTable
configDiffServTable=_ConfigDiffServTable_Object((1,3,6,1,4,1,674,10895,5,11,31))
if mibBuilder.loadTexts:configDiffServTable.setStatus(_A)
_ConfigDiffServEntry_Object=MibTableRow
configDiffServEntry=_ConfigDiffServEntry_Object((1,3,6,1,4,1,674,10895,5,11,31,1))
configDiffServEntry.setIndexNames((0,_H,_V))
if mibBuilder.loadTexts:configDiffServEntry.setStatus(_A)
_ConfigDiffServDSCP_Type=Integer32
_ConfigDiffServDSCP_Object=MibTableColumn
configDiffServDSCP=_ConfigDiffServDSCP_Object((1,3,6,1,4,1,674,10895,5,11,31,1,1),_ConfigDiffServDSCP_Type())
configDiffServDSCP.setMaxAccess(_F)
if mibBuilder.loadTexts:configDiffServDSCP.setStatus(_A)
class _ConfigDiffServPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('high',2)))
_ConfigDiffServPriority_Type.__name__=_C
_ConfigDiffServPriority_Object=MibTableColumn
configDiffServPriority=_ConfigDiffServPriority_Object((1,3,6,1,4,1,674,10895,5,11,31,1,2),_ConfigDiffServPriority_Type())
configDiffServPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:configDiffServPriority.setStatus(_A)
_ConfigTftpServerIpAddress_Type=IpAddress
_ConfigTftpServerIpAddress_Object=MibScalar
configTftpServerIpAddress=_ConfigTftpServerIpAddress_Object((1,3,6,1,4,1,674,10895,5,11,32),_ConfigTftpServerIpAddress_Type())
configTftpServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:configTftpServerIpAddress.setStatus(_A)
class _ConfigTftpServerFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ConfigTftpServerFileName_Type.__name__=_G
_ConfigTftpServerFileName_Object=MibScalar
configTftpServerFileName=_ConfigTftpServerFileName_Object((1,3,6,1,4,1,674,10895,5,11,33),_ConfigTftpServerFileName_Type())
configTftpServerFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:configTftpServerFileName.setStatus(_A)
class _ConfigTftpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('download',1),('upload',2)))
_ConfigTftpOperation_Type.__name__=_C
_ConfigTftpOperation_Object=MibScalar
configTftpOperation=_ConfigTftpOperation_Object((1,3,6,1,4,1,674,10895,5,11,34),_ConfigTftpOperation_Type())
configTftpOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:configTftpOperation.setStatus(_A)
class _ConfigIpFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ConfigIpFilter_Type.__name__=_C
_ConfigIpFilter_Object=MibScalar
configIpFilter=_ConfigIpFilter_Object((1,3,6,1,4,1,674,10895,5,11,35),_ConfigIpFilter_Type())
configIpFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFilter.setStatus(_A)
_ConfigIpFilterTable_Object=MibTable
configIpFilterTable=_ConfigIpFilterTable_Object((1,3,6,1,4,1,674,10895,5,11,36))
if mibBuilder.loadTexts:configIpFilterTable.setStatus(_A)
_ConfigIpFilterEntry_Object=MibTableRow
configIpFilterEntry=_ConfigIpFilterEntry_Object((1,3,6,1,4,1,674,10895,5,11,36,1))
configIpFilterEntry.setIndexNames((0,_H,_W))
if mibBuilder.loadTexts:configIpFilterEntry.setStatus(_A)
_ConfigIpFilterIpAddress_Type=IpAddress
_ConfigIpFilterIpAddress_Object=MibTableColumn
configIpFilterIpAddress=_ConfigIpFilterIpAddress_Object((1,3,6,1,4,1,674,10895,5,11,36,1,1),_ConfigIpFilterIpAddress_Type())
configIpFilterIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:configIpFilterIpAddress.setStatus(_A)
class _ConfigIpFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6)));namedValues=NamedValues(*((_K,1),(_L,6)))
_ConfigIpFilterStatus_Type.__name__=_C
_ConfigIpFilterStatus_Object=MibTableColumn
configIpFilterStatus=_ConfigIpFilterStatus_Object((1,3,6,1,4,1,674,10895,5,11,36,1,2),_ConfigIpFilterStatus_Type())
configIpFilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFilterStatus.setStatus(_A)
_DellVlanGroup_ObjectIdentity=ObjectIdentity
dellVlanGroup=_DellVlanGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5,13))
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,674,10895,5,13,1))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,674,10895,5,13,1,1))
vlanEntry.setIndexNames((0,_H,_X))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
_VlanId_Type=Integer32
_VlanId_Object=MibTableColumn
vlanId=_VlanId_Object((1,3,6,1,4,1,674,10895,5,13,1,1,1),_VlanId_Type())
vlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanId.setStatus(_A)
class _VlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VlanName_Type.__name__=_G
_VlanName_Object=MibTableColumn
vlanName=_VlanName_Object((1,3,6,1,4,1,674,10895,5,13,1,1,2),_VlanName_Type())
vlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanName.setStatus(_A)
class _VlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_K,1),(_Y,4),(_L,6)))
_VlanStatus_Type.__name__=_C
_VlanStatus_Object=MibTableColumn
vlanStatus=_VlanStatus_Object((1,3,6,1,4,1,674,10895,5,13,1,1,3),_VlanStatus_Type())
vlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanStatus.setStatus(_A)
_VlanPortTable_Object=MibTable
vlanPortTable=_VlanPortTable_Object((1,3,6,1,4,1,674,10895,5,13,2))
if mibBuilder.loadTexts:vlanPortTable.setStatus(_A)
_VlanPortEntry_Object=MibTableRow
vlanPortEntry=_VlanPortEntry_Object((1,3,6,1,4,1,674,10895,5,13,2,1))
vlanPortEntry.setIndexNames((0,_H,_Z),(0,_H,_a))
if mibBuilder.loadTexts:vlanPortEntry.setStatus(_A)
_VlanPortPortId_Type=Integer32
_VlanPortPortId_Object=MibTableColumn
vlanPortPortId=_VlanPortPortId_Object((1,3,6,1,4,1,674,10895,5,13,2,1,1),_VlanPortPortId_Type())
vlanPortPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanPortPortId.setStatus(_A)
_VlanPortVlanId_Type=Integer32
_VlanPortVlanId_Object=MibTableColumn
vlanPortVlanId=_VlanPortVlanId_Object((1,3,6,1,4,1,674,10895,5,13,2,1,2),_VlanPortVlanId_Type())
vlanPortVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanPortVlanId.setStatus(_A)
class _VlanPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_K,1),(_Y,4),(_L,6)))
_VlanPortStatus_Type.__name__=_C
_VlanPortStatus_Object=MibTableColumn
vlanPortStatus=_VlanPortStatus_Object((1,3,6,1,4,1,674,10895,5,13,2,1,3),_VlanPortStatus_Type())
vlanPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortStatus.setStatus(_A)
class _VlanPortTaggedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('untagged',1),('tagged',2)))
_VlanPortTaggedMode_Type.__name__=_C
_VlanPortTaggedMode_Object=MibTableColumn
vlanPortTaggedMode=_VlanPortTaggedMode_Object((1,3,6,1,4,1,674,10895,5,13,2,1,4),_VlanPortTaggedMode_Type())
vlanPortTaggedMode.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortTaggedMode.setStatus(_A)
_DellPortTrunkGroup_ObjectIdentity=ObjectIdentity
dellPortTrunkGroup=_DellPortTrunkGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5,14))
_PortTrunkTable_Object=MibTable
portTrunkTable=_PortTrunkTable_Object((1,3,6,1,4,1,674,10895,5,14,1))
if mibBuilder.loadTexts:portTrunkTable.setStatus(_A)
_PortTrunkEntry_Object=MibTableRow
portTrunkEntry=_PortTrunkEntry_Object((1,3,6,1,4,1,674,10895,5,14,1,1))
portTrunkEntry.setIndexNames((0,_H,_b),(0,_H,_c))
if mibBuilder.loadTexts:portTrunkEntry.setStatus(_A)
_PortTrunkId_Type=Integer32
_PortTrunkId_Object=MibTableColumn
portTrunkId=_PortTrunkId_Object((1,3,6,1,4,1,674,10895,5,14,1,1,1),_PortTrunkId_Type())
portTrunkId.setMaxAccess(_F)
if mibBuilder.loadTexts:portTrunkId.setStatus(_A)
_PortTrunkMember_Type=Integer32
_PortTrunkMember_Object=MibTableColumn
portTrunkMember=_PortTrunkMember_Object((1,3,6,1,4,1,674,10895,5,14,1,1,2),_PortTrunkMember_Type())
portTrunkMember.setMaxAccess(_F)
if mibBuilder.loadTexts:portTrunkMember.setStatus(_A)
_PortTrunkMemberValue_Type=Integer32
_PortTrunkMemberValue_Object=MibTableColumn
portTrunkMemberValue=_PortTrunkMemberValue_Object((1,3,6,1,4,1,674,10895,5,14,1,1,3),_PortTrunkMemberValue_Type())
portTrunkMemberValue.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrunkMemberValue.setStatus(_A)
addressIntrusion=NotificationType((1,3,6,1,4,1,674,0,0))
addressIntrusion.setObjects((_H,'ifIndex'))
if mibBuilder.loadTexts:addressIntrusion.setStatus('')
mibBuilder.exportSymbols(_H,**{'OwnerString':OwnerString,'MacAddress':MacAddress,'dell':dell,'addressIntrusion':addressIntrusion,'dellLan':dellLan,'powerconnect3048':powerconnect3048,'dellCommGroup':dellCommGroup,'commTable':commTable,'commEntry':commEntry,_M:commIndex,'commName':commName,'commGet':commGet,'commSet':commSet,'commTrap':commTrap,'commStatus':commStatus,'dellHostGroup':dellHostGroup,'hostTable':hostTable,'hostEntry':hostEntry,_N:hostIndex,'hostName':hostName,'hostIP':hostIP,'hostComm':hostComm,'hostStatus':hostStatus,'hostAuthorization':hostAuthorization,'dellMiscGroup':dellMiscGroup,'miscBaud':miscBaud,'miscReset':miscReset,'miscStatisticsReset':miscStatisticsReset,'miscSwitchOperState':miscSwitchOperState,'dellSpanGroup':dellSpanGroup,'spanOnOff':spanOnOff,'dellConfigGroup':dellConfigGroup,'configVerSwPrimary':configVerSwPrimary,'configVerHwChipSet':configVerHwChipSet,'configBootMode':configBootMode,'configBootFtpServerIp':configBootFtpServerIp,'configBootImageFileName':configBootImageFileName,'configPortTable':configPortTable,'configPortEntry':configPortEntry,_O:configPort,'configPortDuplex':configPortDuplex,'configPortRuntFilt':configPortRuntFilt,'configPortSrcSecurity':configPortSrcSecurity,'configPortDataRate':configPortDataRate,'configForwardingMode':configForwardingMode,'configPortDuplexOper':configPortDuplexOper,'configPortDataRateOper':configPortDataRateOper,'configPortStateOper':configPortStateOper,'configPortFlowControl':configPortFlowControl,'configPortDefaultVlanId':configPortDefaultVlanId,'configPortComments':configPortComments,'configPortAutoNegotiation':configPortAutoNegotiation,'configPortHOLBlocking':configPortHOLBlocking,'configPortFlowControlOper':configPortFlowControlOper,'configPortGBIC':configPortGBIC,'configPortFastLink':configPortFastLink,'configPortPriority':configPortPriority,'configRmonOnOff':configRmonOnOff,'configMirroringOnOff':configMirroringOnOff,'configMirrorSrc':configMirrorSrc,'configMirrorMon':configMirrorMon,'configIpAssignmentMode':configIpAssignmentMode,'configPhysAddress':configPhysAddress,'configPasswordUser':configPasswordUser,'configPasswordAdmin':configPasswordAdmin,'configIpAddress':configIpAddress,'configNetMask':configNetMask,'configGateway':configGateway,'configSave':configSave,'configVerifyPassword':configVerifyPassword,'configVerBootRomImage':configVerBootRomImage,'configRestoreDefaults':configRestoreDefaults,'configIGMPOnOff':configIGMPOnOff,'configWebOnOff':configWebOnOff,'configHighPriorityOptimization':configHighPriorityOptimization,'configDynamicAddressLearning':configDynamicAddressLearning,'configUserAuthenticationMode':configUserAuthenticationMode,'configRadiusServerIpAddress':configRadiusServerIpAddress,'configRadiusSharedSecret':configRadiusSharedSecret,'configTelnetConsole':configTelnetConsole,'configDiffServTable':configDiffServTable,'configDiffServEntry':configDiffServEntry,_V:configDiffServDSCP,'configDiffServPriority':configDiffServPriority,'configTftpServerIpAddress':configTftpServerIpAddress,'configTftpServerFileName':configTftpServerFileName,'configTftpOperation':configTftpOperation,'configIpFilter':configIpFilter,'configIpFilterTable':configIpFilterTable,'configIpFilterEntry':configIpFilterEntry,_W:configIpFilterIpAddress,'configIpFilterStatus':configIpFilterStatus,'dellVlanGroup':dellVlanGroup,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_X:vlanId,'vlanName':vlanName,'vlanStatus':vlanStatus,'vlanPortTable':vlanPortTable,'vlanPortEntry':vlanPortEntry,_Z:vlanPortPortId,_a:vlanPortVlanId,'vlanPortStatus':vlanPortStatus,'vlanPortTaggedMode':vlanPortTaggedMode,'dellPortTrunkGroup':dellPortTrunkGroup,'portTrunkTable':portTrunkTable,'portTrunkEntry':portTrunkEntry,_b:portTrunkId,_c:portTrunkMember,'portTrunkMemberValue':portTrunkMemberValue})