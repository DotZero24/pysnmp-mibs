_K='e1t1SerialStatsID'
_J='e1t1GroupID'
_I='e1t1SerialID'
_H='NotificationType'
_G='OctetString'
_F='donothing'
_E='REDLINE-E1T1-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
_Redline_ObjectIdentity=ObjectIdentity
redline=_Redline_ObjectIdentity((1,3,6,1,4,1,10728))
_RedlineProducts_ObjectIdentity=ObjectIdentity
redlineProducts=_RedlineProducts_ObjectIdentity((1,3,6,1,4,1,10728,1))
_RedlineMgmt_ObjectIdentity=ObjectIdentity
redlineMgmt=_RedlineMgmt_ObjectIdentity((1,3,6,1,4,1,10728,2))
_RedlineE1T1_ObjectIdentity=ObjectIdentity
redlineE1T1=_RedlineE1T1_ObjectIdentity((1,3,6,1,4,1,10728,2,52))
_E1t1General_ObjectIdentity=ObjectIdentity
e1t1General=_E1t1General_ObjectIdentity((1,3,6,1,4,1,10728,2,52,1))
class _E1t1VlanIdData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_E1t1VlanIdData_Type.__name__=_D
_E1t1VlanIdData_Object=MibScalar
e1t1VlanIdData=_E1t1VlanIdData_Object((1,3,6,1,4,1,10728,2,52,1,1),_E1t1VlanIdData_Type())
e1t1VlanIdData.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1VlanIdData.setStatus(_A)
class _E1t1VlanIdVoice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_E1t1VlanIdVoice_Type.__name__=_D
_E1t1VlanIdVoice_Object=MibScalar
e1t1VlanIdVoice=_E1t1VlanIdVoice_Object((1,3,6,1,4,1,10728,2,52,1,2),_E1t1VlanIdVoice_Type())
e1t1VlanIdVoice.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1VlanIdVoice.setStatus(_A)
class _E1t1Clock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_E1t1Clock_Type.__name__=_D
_E1t1Clock_Object=MibScalar
e1t1Clock=_E1t1Clock_Object((1,3,6,1,4,1,10728,2,52,1,3),_E1t1Clock_Type())
e1t1Clock.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1Clock.setStatus(_A)
class _E1t1SyncOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_E1t1SyncOn_Type.__name__=_D
_E1t1SyncOn_Object=MibScalar
e1t1SyncOn=_E1t1SyncOn_Object((1,3,6,1,4,1,10728,2,52,1,4),_E1t1SyncOn_Type())
e1t1SyncOn.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1SyncOn.setStatus(_A)
_E1t1IdleCode_Type=Integer32
_E1t1IdleCode_Object=MibScalar
e1t1IdleCode=_E1t1IdleCode_Object((1,3,6,1,4,1,10728,2,52,1,5),_E1t1IdleCode_Type())
e1t1IdleCode.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1IdleCode.setStatus(_A)
class _E1t1Hostname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_E1t1Hostname_Type.__name__=_G
_E1t1Hostname_Object=MibScalar
e1t1Hostname=_E1t1Hostname_Object((1,3,6,1,4,1,10728,2,52,1,6),_E1t1Hostname_Type())
e1t1Hostname.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1Hostname.setStatus(_A)
_E1t1IpAddress_Type=IpAddress
_E1t1IpAddress_Object=MibScalar
e1t1IpAddress=_E1t1IpAddress_Object((1,3,6,1,4,1,10728,2,52,1,7),_E1t1IpAddress_Type())
e1t1IpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1IpAddress.setStatus(_A)
_E1t1IpMask_Type=IpAddress
_E1t1IpMask_Object=MibScalar
e1t1IpMask=_E1t1IpMask_Object((1,3,6,1,4,1,10728,2,52,1,8),_E1t1IpMask_Type())
e1t1IpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1IpMask.setStatus(_A)
_E1t1IpGateway_Type=IpAddress
_E1t1IpGateway_Object=MibScalar
e1t1IpGateway=_E1t1IpGateway_Object((1,3,6,1,4,1,10728,2,52,1,9),_E1t1IpGateway_Type())
e1t1IpGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1IpGateway.setStatus(_A)
_E1t1OptionKey_Type=Integer32
_E1t1OptionKey_Object=MibScalar
e1t1OptionKey=_E1t1OptionKey_Object((1,3,6,1,4,1,10728,2,52,1,10),_E1t1OptionKey_Type())
e1t1OptionKey.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1OptionKey.setStatus(_A)
_E1t1Line_Type=Integer32
_E1t1Line_Object=MibScalar
e1t1Line=_E1t1Line_Object((1,3,6,1,4,1,10728,2,52,1,11),_E1t1Line_Type())
e1t1Line.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1Line.setStatus(_A)
class _E1t1SoftwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_E1t1SoftwareVersion_Type.__name__=_G
_E1t1SoftwareVersion_Object=MibScalar
e1t1SoftwareVersion=_E1t1SoftwareVersion_Object((1,3,6,1,4,1,10728,2,52,1,12),_E1t1SoftwareVersion_Type())
e1t1SoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1SoftwareVersion.setStatus(_A)
_E1t1SerialTable_Object=MibTable
e1t1SerialTable=_E1t1SerialTable_Object((1,3,6,1,4,1,10728,2,52,2))
if mibBuilder.loadTexts:e1t1SerialTable.setStatus(_A)
_E1t1SerialEntry_Object=MibTableRow
e1t1SerialEntry=_E1t1SerialEntry_Object((1,3,6,1,4,1,10728,2,52,2,1))
e1t1SerialEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:e1t1SerialEntry.setStatus(_A)
class _E1t1SerialID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_E1t1SerialID_Type.__name__=_D
_E1t1SerialID_Object=MibTableColumn
e1t1SerialID=_E1t1SerialID_Object((1,3,6,1,4,1,10728,2,52,2,1,1),_E1t1SerialID_Type())
e1t1SerialID.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1SerialID.setStatus(_A)
class _E1t1SerialCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_E1t1SerialCoding_Type.__name__=_D
_E1t1SerialCoding_Object=MibTableColumn
e1t1SerialCoding=_E1t1SerialCoding_Object((1,3,6,1,4,1,10728,2,52,2,1,2),_E1t1SerialCoding_Type())
e1t1SerialCoding.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1SerialCoding.setStatus(_A)
class _E1t1SerialFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_E1t1SerialFraming_Type.__name__=_D
_E1t1SerialFraming_Object=MibTableColumn
e1t1SerialFraming=_E1t1SerialFraming_Object((1,3,6,1,4,1,10728,2,52,2,1,3),_E1t1SerialFraming_Type())
e1t1SerialFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1SerialFraming.setStatus(_A)
class _E1t1SerialLBO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_E1t1SerialLBO_Type.__name__=_D
_E1t1SerialLBO_Object=MibTableColumn
e1t1SerialLBO=_E1t1SerialLBO_Object((1,3,6,1,4,1,10728,2,52,2,1,4),_E1t1SerialLBO_Type())
e1t1SerialLBO.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1SerialLBO.setStatus(_A)
_E1t1GroupTable_Object=MibTable
e1t1GroupTable=_E1t1GroupTable_Object((1,3,6,1,4,1,10728,2,52,3))
if mibBuilder.loadTexts:e1t1GroupTable.setStatus(_A)
_E1t1GroupEntry_Object=MibTableRow
e1t1GroupEntry=_E1t1GroupEntry_Object((1,3,6,1,4,1,10728,2,52,3,1))
e1t1GroupEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:e1t1GroupEntry.setStatus(_A)
class _E1t1GroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_E1t1GroupID_Type.__name__=_D
_E1t1GroupID_Object=MibTableColumn
e1t1GroupID=_E1t1GroupID_Object((1,3,6,1,4,1,10728,2,52,3,1,1),_E1t1GroupID_Type())
e1t1GroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1GroupID.setStatus(_A)
class _E1t1GroupTsBegin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_E1t1GroupTsBegin_Type.__name__=_D
_E1t1GroupTsBegin_Object=MibTableColumn
e1t1GroupTsBegin=_E1t1GroupTsBegin_Object((1,3,6,1,4,1,10728,2,52,3,1,2),_E1t1GroupTsBegin_Type())
e1t1GroupTsBegin.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1GroupTsBegin.setStatus(_A)
class _E1t1GroupTsNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_E1t1GroupTsNum_Type.__name__=_D
_E1t1GroupTsNum_Object=MibTableColumn
e1t1GroupTsNum=_E1t1GroupTsNum_Object((1,3,6,1,4,1,10728,2,52,3,1,3),_E1t1GroupTsNum_Type())
e1t1GroupTsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1GroupTsNum.setStatus(_A)
class _E1t1GroupDestGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_E1t1GroupDestGroup_Type.__name__=_D
_E1t1GroupDestGroup_Object=MibTableColumn
e1t1GroupDestGroup=_E1t1GroupDestGroup_Object((1,3,6,1,4,1,10728,2,52,3,1,4),_E1t1GroupDestGroup_Type())
e1t1GroupDestGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1GroupDestGroup.setStatus(_A)
_E1t1GroupDestIp_Type=IpAddress
_E1t1GroupDestIp_Object=MibTableColumn
e1t1GroupDestIp=_E1t1GroupDestIp_Object((1,3,6,1,4,1,10728,2,52,3,1,5),_E1t1GroupDestIp_Type())
e1t1GroupDestIp.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1GroupDestIp.setStatus(_A)
class _E1t1GroupJitterBuffer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_E1t1GroupJitterBuffer_Type.__name__=_D
_E1t1GroupJitterBuffer_Object=MibTableColumn
e1t1GroupJitterBuffer=_E1t1GroupJitterBuffer_Object((1,3,6,1,4,1,10728,2,52,3,1,6),_E1t1GroupJitterBuffer_Type())
e1t1GroupJitterBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1GroupJitterBuffer.setStatus(_A)
class _E1t1GroupPacketLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024))
_E1t1GroupPacketLength_Type.__name__=_D
_E1t1GroupPacketLength_Object=MibTableColumn
e1t1GroupPacketLength=_E1t1GroupPacketLength_Object((1,3,6,1,4,1,10728,2,52,3,1,7),_E1t1GroupPacketLength_Type())
e1t1GroupPacketLength.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1GroupPacketLength.setStatus(_A)
_E1t1GroupRowStatus_Type=RowStatus
_E1t1GroupRowStatus_Object=MibTableColumn
e1t1GroupRowStatus=_E1t1GroupRowStatus_Object((1,3,6,1,4,1,10728,2,52,3,1,8),_E1t1GroupRowStatus_Type())
e1t1GroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1GroupRowStatus.setStatus(_A)
_E1t1StatsTable_Object=MibTable
e1t1StatsTable=_E1t1StatsTable_Object((1,3,6,1,4,1,10728,2,52,4))
if mibBuilder.loadTexts:e1t1StatsTable.setStatus(_A)
_E1t1StatsEntry_Object=MibTableRow
e1t1StatsEntry=_E1t1StatsEntry_Object((1,3,6,1,4,1,10728,2,52,4,1))
e1t1StatsEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:e1t1StatsEntry.setStatus(_A)
class _E1t1SerialStatsID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_E1t1SerialStatsID_Type.__name__=_D
_E1t1SerialStatsID_Object=MibTableColumn
e1t1SerialStatsID=_E1t1SerialStatsID_Object((1,3,6,1,4,1,10728,2,52,4,1,1),_E1t1SerialStatsID_Type())
e1t1SerialStatsID.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1SerialStatsID.setStatus(_A)
_E1t1TdmsLOS_Type=Integer32
_E1t1TdmsLOS_Object=MibTableColumn
e1t1TdmsLOS=_E1t1TdmsLOS_Object((1,3,6,1,4,1,10728,2,52,4,1,2),_E1t1TdmsLOS_Type())
e1t1TdmsLOS.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1TdmsLOS.setStatus(_A)
_E1t1TdmsLFA_Type=Integer32
_E1t1TdmsLFA_Object=MibTableColumn
e1t1TdmsLFA=_E1t1TdmsLFA_Object((1,3,6,1,4,1,10728,2,52,4,1,3),_E1t1TdmsLFA_Type())
e1t1TdmsLFA.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1TdmsLFA.setStatus(_A)
_E1t1TdmsLOMF_Type=Integer32
_E1t1TdmsLOMF_Object=MibTableColumn
e1t1TdmsLOMF=_E1t1TdmsLOMF_Object((1,3,6,1,4,1,10728,2,52,4,1,4),_E1t1TdmsLOMF_Type())
e1t1TdmsLOMF.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1TdmsLOMF.setStatus(_A)
_E1t1TdmsRAI_Type=Integer32
_E1t1TdmsRAI_Object=MibTableColumn
e1t1TdmsRAI=_E1t1TdmsRAI_Object((1,3,6,1,4,1,10728,2,52,4,1,5),_E1t1TdmsRAI_Type())
e1t1TdmsRAI.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1TdmsRAI.setStatus(_A)
_E1t1TdmsAIS_Type=Integer32
_E1t1TdmsAIS_Object=MibTableColumn
e1t1TdmsAIS=_E1t1TdmsAIS_Object((1,3,6,1,4,1,10728,2,52,4,1,6),_E1t1TdmsAIS_Type())
e1t1TdmsAIS.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1TdmsAIS.setStatus(_A)
_E1t1TdmsES_Type=Integer32
_E1t1TdmsES_Object=MibTableColumn
e1t1TdmsES=_E1t1TdmsES_Object((1,3,6,1,4,1,10728,2,52,4,1,7),_E1t1TdmsES_Type())
e1t1TdmsES.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1TdmsES.setStatus(_A)
_E1t1TdmsFEC_Type=Integer32
_E1t1TdmsFEC_Object=MibTableColumn
e1t1TdmsFEC=_E1t1TdmsFEC_Object((1,3,6,1,4,1,10728,2,52,4,1,8),_E1t1TdmsFEC_Type())
e1t1TdmsFEC.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1TdmsFEC.setStatus(_A)
_E1t1TdmsCVC_Type=Integer32
_E1t1TdmsCVC_Object=MibTableColumn
e1t1TdmsCVC=_E1t1TdmsCVC_Object((1,3,6,1,4,1,10728,2,52,4,1,9),_E1t1TdmsCVC_Type())
e1t1TdmsCVC.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1TdmsCVC.setStatus(_A)
_E1t1Stats_ObjectIdentity=ObjectIdentity
e1t1Stats=_E1t1Stats_ObjectIdentity((1,3,6,1,4,1,10728,2,52,5))
_E1t1EthRate_Type=Integer32
_E1t1EthRate_Object=MibScalar
e1t1EthRate=_E1t1EthRate_Object((1,3,6,1,4,1,10728,2,52,5,1),_E1t1EthRate_Type())
e1t1EthRate.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthRate.setStatus(_A)
_E1t1EthMode_Type=Integer32
_E1t1EthMode_Object=MibScalar
e1t1EthMode=_E1t1EthMode_Object((1,3,6,1,4,1,10728,2,52,5,2),_E1t1EthMode_Type())
e1t1EthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthMode.setStatus(_A)
_E1t1EthState_Type=Integer32
_E1t1EthState_Object=MibScalar
e1t1EthState=_E1t1EthState_Object((1,3,6,1,4,1,10728,2,52,5,3),_E1t1EthState_Type())
e1t1EthState.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthState.setStatus(_A)
_E1t1EthMAC_Type=Integer32
_E1t1EthMAC_Object=MibScalar
e1t1EthMAC=_E1t1EthMAC_Object((1,3,6,1,4,1,10728,2,52,5,4),_E1t1EthMAC_Type())
e1t1EthMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthMAC.setStatus(_A)
_E1t1EthFROK_Type=Integer32
_E1t1EthFROK_Object=MibScalar
e1t1EthFROK=_E1t1EthFROK_Object((1,3,6,1,4,1,10728,2,52,5,5),_E1t1EthFROK_Type())
e1t1EthFROK.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthFROK.setStatus(_A)
_E1t1EthBROK_Type=Integer32
_E1t1EthBROK_Object=MibScalar
e1t1EthBROK=_E1t1EthBROK_Object((1,3,6,1,4,1,10728,2,52,5,6),_E1t1EthBROK_Type())
e1t1EthBROK.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthBROK.setStatus(_A)
_E1t1EthAERR_Type=Integer32
_E1t1EthAERR_Object=MibScalar
e1t1EthAERR=_E1t1EthAERR_Object((1,3,6,1,4,1,10728,2,52,5,7),_E1t1EthAERR_Type())
e1t1EthAERR.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthAERR.setStatus(_A)
_E1t1EthCERR_Type=Integer32
_E1t1EthCERR_Object=MibScalar
e1t1EthCERR=_E1t1EthCERR_Object((1,3,6,1,4,1,10728,2,52,5,8),_E1t1EthCERR_Type())
e1t1EthCERR.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthCERR.setStatus(_A)
_E1t1EthFTOK_Type=Integer32
_E1t1EthFTOK_Object=MibScalar
e1t1EthFTOK=_E1t1EthFTOK_Object((1,3,6,1,4,1,10728,2,52,5,9),_E1t1EthFTOK_Type())
e1t1EthFTOK.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthFTOK.setStatus(_A)
_E1t1EthBTOK_Type=Integer32
_E1t1EthBTOK_Object=MibScalar
e1t1EthBTOK=_E1t1EthBTOK_Object((1,3,6,1,4,1,10728,2,52,5,10),_E1t1EthBTOK_Type())
e1t1EthBTOK.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthBTOK.setStatus(_A)
_E1t1EthSCOL_Type=Integer32
_E1t1EthSCOL_Object=MibScalar
e1t1EthSCOL=_E1t1EthSCOL_Object((1,3,6,1,4,1,10728,2,52,5,11),_E1t1EthSCOL_Type())
e1t1EthSCOL.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthSCOL.setStatus(_A)
_E1t1EthMCOL_Type=Integer32
_E1t1EthMCOL_Object=MibScalar
e1t1EthMCOL=_E1t1EthMCOL_Object((1,3,6,1,4,1,10728,2,52,5,12),_E1t1EthMCOL_Type())
e1t1EthMCOL.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthMCOL.setStatus(_A)
_E1t1EthTDEF_Type=Integer32
_E1t1EthTDEF_Object=MibScalar
e1t1EthTDEF=_E1t1EthTDEF_Object((1,3,6,1,4,1,10728,2,52,5,13),_E1t1EthTDEF_Type())
e1t1EthTDEF.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthTDEF.setStatus(_A)
_E1t1EthLCOL_Type=Integer32
_E1t1EthLCOL_Object=MibScalar
e1t1EthLCOL=_E1t1EthLCOL_Object((1,3,6,1,4,1,10728,2,52,5,14),_E1t1EthLCOL_Type())
e1t1EthLCOL.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1EthLCOL.setStatus(_A)
class _E1t1FanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_E1t1FanStatus_Type.__name__=_D
_E1t1FanStatus_Object=MibScalar
e1t1FanStatus=_E1t1FanStatus_Object((1,3,6,1,4,1,10728,2,52,5,15),_E1t1FanStatus_Type())
e1t1FanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1FanStatus.setStatus(_A)
_E1t1LastSaveErr_Type=Integer32
_E1t1LastSaveErr_Object=MibScalar
e1t1LastSaveErr=_E1t1LastSaveErr_Object((1,3,6,1,4,1,10728,2,52,5,16),_E1t1LastSaveErr_Type())
e1t1LastSaveErr.setMaxAccess(_B)
if mibBuilder.loadTexts:e1t1LastSaveErr.setStatus(_A)
_E1t1Commands_ObjectIdentity=ObjectIdentity
e1t1Commands=_E1t1Commands_ObjectIdentity((1,3,6,1,4,1,10728,2,52,6))
class _E1t1SaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('saveConfig',2)))
_E1t1SaveConfig_Type.__name__=_D
_E1t1SaveConfig_Object=MibScalar
e1t1SaveConfig=_E1t1SaveConfig_Object((1,3,6,1,4,1,10728,2,52,6,1),_E1t1SaveConfig_Type())
e1t1SaveConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1SaveConfig.setStatus(_A)
class _E1t1ActivateConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('activeConfig',2)))
_E1t1ActivateConfig_Type.__name__=_D
_E1t1ActivateConfig_Object=MibScalar
e1t1ActivateConfig=_E1t1ActivateConfig_Object((1,3,6,1,4,1,10728,2,52,6,2),_E1t1ActivateConfig_Type())
e1t1ActivateConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1ActivateConfig.setStatus(_A)
class _E1t1ResetBoard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('reset',2)))
_E1t1ResetBoard_Type.__name__=_D
_E1t1ResetBoard_Object=MibScalar
e1t1ResetBoard=_E1t1ResetBoard_Object((1,3,6,1,4,1,10728,2,52,6,3),_E1t1ResetBoard_Type())
e1t1ResetBoard.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1ResetBoard.setStatus(_A)
class _E1t1ResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,35))
_E1t1ResetStats_Type.__name__=_D
_E1t1ResetStats_Object=MibScalar
e1t1ResetStats=_E1t1ResetStats_Object((1,3,6,1,4,1,10728,2,52,6,4),_E1t1ResetStats_Type())
e1t1ResetStats.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1ResetStats.setStatus(_A)
class _E1t1ReStartConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('reset',2)))
_E1t1ReStartConfig_Type.__name__=_D
_E1t1ReStartConfig_Object=MibScalar
e1t1ReStartConfig=_E1t1ReStartConfig_Object((1,3,6,1,4,1,10728,2,52,6,5),_E1t1ReStartConfig_Type())
e1t1ReStartConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:e1t1ReStartConfig.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'redline':redline,'redlineProducts':redlineProducts,'redlineMgmt':redlineMgmt,'redlineE1T1':redlineE1T1,'e1t1General':e1t1General,'e1t1VlanIdData':e1t1VlanIdData,'e1t1VlanIdVoice':e1t1VlanIdVoice,'e1t1Clock':e1t1Clock,'e1t1SyncOn':e1t1SyncOn,'e1t1IdleCode':e1t1IdleCode,'e1t1Hostname':e1t1Hostname,'e1t1IpAddress':e1t1IpAddress,'e1t1IpMask':e1t1IpMask,'e1t1IpGateway':e1t1IpGateway,'e1t1OptionKey':e1t1OptionKey,'e1t1Line':e1t1Line,'e1t1SoftwareVersion':e1t1SoftwareVersion,'e1t1SerialTable':e1t1SerialTable,'e1t1SerialEntry':e1t1SerialEntry,_I:e1t1SerialID,'e1t1SerialCoding':e1t1SerialCoding,'e1t1SerialFraming':e1t1SerialFraming,'e1t1SerialLBO':e1t1SerialLBO,'e1t1GroupTable':e1t1GroupTable,'e1t1GroupEntry':e1t1GroupEntry,_J:e1t1GroupID,'e1t1GroupTsBegin':e1t1GroupTsBegin,'e1t1GroupTsNum':e1t1GroupTsNum,'e1t1GroupDestGroup':e1t1GroupDestGroup,'e1t1GroupDestIp':e1t1GroupDestIp,'e1t1GroupJitterBuffer':e1t1GroupJitterBuffer,'e1t1GroupPacketLength':e1t1GroupPacketLength,'e1t1GroupRowStatus':e1t1GroupRowStatus,'e1t1StatsTable':e1t1StatsTable,'e1t1StatsEntry':e1t1StatsEntry,_K:e1t1SerialStatsID,'e1t1TdmsLOS':e1t1TdmsLOS,'e1t1TdmsLFA':e1t1TdmsLFA,'e1t1TdmsLOMF':e1t1TdmsLOMF,'e1t1TdmsRAI':e1t1TdmsRAI,'e1t1TdmsAIS':e1t1TdmsAIS,'e1t1TdmsES':e1t1TdmsES,'e1t1TdmsFEC':e1t1TdmsFEC,'e1t1TdmsCVC':e1t1TdmsCVC,'e1t1Stats':e1t1Stats,'e1t1EthRate':e1t1EthRate,'e1t1EthMode':e1t1EthMode,'e1t1EthState':e1t1EthState,'e1t1EthMAC':e1t1EthMAC,'e1t1EthFROK':e1t1EthFROK,'e1t1EthBROK':e1t1EthBROK,'e1t1EthAERR':e1t1EthAERR,'e1t1EthCERR':e1t1EthCERR,'e1t1EthFTOK':e1t1EthFTOK,'e1t1EthBTOK':e1t1EthBTOK,'e1t1EthSCOL':e1t1EthSCOL,'e1t1EthMCOL':e1t1EthMCOL,'e1t1EthTDEF':e1t1EthTDEF,'e1t1EthLCOL':e1t1EthLCOL,'e1t1FanStatus':e1t1FanStatus,'e1t1LastSaveErr':e1t1LastSaveErr,'e1t1Commands':e1t1Commands,'e1t1SaveConfig':e1t1SaveConfig,'e1t1ActivateConfig':e1t1ActivateConfig,'e1t1ResetBoard':e1t1ResetBoard,'e1t1ResetStats':e1t1ResetStats,'e1t1ReStartConfig':e1t1ReStartConfig})