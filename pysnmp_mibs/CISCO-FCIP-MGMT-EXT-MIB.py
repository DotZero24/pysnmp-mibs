_AH='cfmFcipLinkExtGroupRev2Sup3'
_AG='cfmFcipEntityExtGroupSup1'
_AF='cfmFcipLinkExtFiconTAVsanLOper4k'
_AE='cfmFcipLinkExtFiconTAVsanLOper2k'
_AD='cfmFcipLinkExtFiconTAVsanL4k'
_AC='cfmFcipLinkExtFiconTAVsanL2k'
_AB='cfmFcipLinkExtTapeReadAccOper'
_AA='cfmFcipLinkStatsTxIPCompRatio'
_A9='cfmFcipLinkStatsRxIPCompRatio'
_A8='cfmFcipLinkExtTapeAccOper'
_A7='cfmFcipLinkExtWriteAccOper'
_A6='cfmFcipLinkExtPhyIfIndex'
_A5='cfmFcipLinkExtIPSec'
_A4='cfmFcipEntityExtTcpMaxJitter'
_A3='cfmFcipMapEntityId'
_A2='cfmFcipLinkExtFlowCtrlBufSize'
_A1='cfmFcipLinkExtTapeAccelerator'
_A0='cfmFcipEntityExtTcpLocalPort'
_z='cfmFcipEntityExtTcpSACKEnable'
_y='cfmFcipEntityExtCWMBurstSize'
_x='cfmFcipEntityExtCWMEnable'
_w='cfmFcipLinkExtIPComp'
_v='cfmFcipLinkExtWriteAccelerator'
_u='cfmFcipLinkExtEthIfIndex'
_t='cfmFcipLinkExtDataQOSField'
_s='cfmFcipLinkExtCntrlQOSField'
_r='cfmFcipLinkExtBPortKAEnable'
_q='cfmFcipLinkExtSpecialFrameEnable'
_p='cfmFcipLinkExtLocalBPortEnable'
_o='cfmFcipLinkExtTcpRemPort'
_n='cfmFcipLinkExtTimestampTolerance'
_m='cfmFcipLinkExtCheckTimestamp'
_l='cfmFcipLinkExtNumTcpConn'
_k='cfmFcipLinkExtPassiveMode'
_j='cfmFcipEntityExtTcpRndTrpTimeEst'
_i='cfmFcipEntityExtTcpMinAvailBW'
_h='cfmFcipEntityExtTcpMaxBW'
_g='cfmFcipEntityExtTcpSendBufSize'
_f='cfmFcipEntityExtTcpMinRTO'
_e='cfmFcipEntityExtPMTUResetTO'
_d='cfmFcipEntityExtPMTUEnable'
_c='cfmFcipEntityExtTcpMaxReTx'
_b='cfmFcipEntityExtTcpKeepAliveTO'
_a='cfmFcipLinkExtStatsEntry'
_Z='cfmFcipLinkExtEntry'
_Y='cfmFcipEntityExtEntry'
_X='cfmFcipLinkMapIndex'
_W='kilobits'
_V='kilobytes'
_U='seconds'
_T='Integer32'
_S='CiscoPort'
_R='cfmFcipLinkExtStatsGroup'
_Q='cfmFcipLinkExtGroupRev2Sup2'
_P='cfmFcipLinkExtMapGroup'
_O='milliseconds'
_N='FcList'
_M='cfmFcipLinkExtGroupRev2Sup1'
_L='cfmFcipLinkExtGroupRev2'
_K='cfmFcipEntityExtCWMGroup'
_J='deprecated'
_I='cfmFcipLinkExtGroupRev1'
_H='cfmFcipLinkExtGroup'
_G='cfmFcipEntityExtGroup'
_F='read-only'
_E='TruthValue'
_D='Unsigned32'
_C='read-create'
_B='current'
_A='CISCO-FCIP-MGMT-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cfmFcipEntityInstanceEntry,cfmFcipLinkEntry=mibBuilder.importSymbols('CISCO-FCIP-MGMT-MIB','cfmFcipEntityInstanceEntry','cfmFcipLinkEntry')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,=mibBuilder.importSymbols('CISCO-TC',_S)
FcList,=mibBuilder.importSymbols('CISCO-ZS-MIB',_N)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_T,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
ciscoFcipMgmtExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,329))
if mibBuilder.loadTexts:ciscoFcipMgmtExtMIB.setRevisions(('2005-10-12 00:00','2005-06-07 00:00','2005-05-14 00:00','2004-09-23 00:00','2004-03-10 00:00','2003-11-05 00:00','2003-09-19 00:00','2003-05-06 00:00','2003-03-25 00:00','2003-01-07 00:00','2002-12-06 00:00'))
_CiscoFcipMgmtExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFcipMgmtExtMIBNotifs=_CiscoFcipMgmtExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,329,0))
_CiscoFcipMgmtExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFcipMgmtExtMIBObjects=_CiscoFcipMgmtExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,329,1))
_CfmFcipMgmtExtConfig_ObjectIdentity=ObjectIdentity
cfmFcipMgmtExtConfig=_CfmFcipMgmtExtConfig_ObjectIdentity((1,3,6,1,4,1,9,9,329,1,1))
_CfmFcipEntityExtTable_Object=MibTable
cfmFcipEntityExtTable=_CfmFcipEntityExtTable_Object((1,3,6,1,4,1,9,9,329,1,1,1))
if mibBuilder.loadTexts:cfmFcipEntityExtTable.setStatus(_B)
_CfmFcipEntityExtEntry_Object=MibTableRow
cfmFcipEntityExtEntry=_CfmFcipEntityExtEntry_Object((1,3,6,1,4,1,9,9,329,1,1,1,1))
if mibBuilder.loadTexts:cfmFcipEntityExtEntry.setStatus(_B)
class _CfmFcipEntityExtTcpKeepAliveTO_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7200))
_CfmFcipEntityExtTcpKeepAliveTO_Type.__name__=_D
_CfmFcipEntityExtTcpKeepAliveTO_Object=MibTableColumn
cfmFcipEntityExtTcpKeepAliveTO=_CfmFcipEntityExtTcpKeepAliveTO_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,1),_CfmFcipEntityExtTcpKeepAliveTO_Type())
cfmFcipEntityExtTcpKeepAliveTO.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpKeepAliveTO.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpKeepAliveTO.setUnits(_U)
class _CfmFcipEntityExtTcpMaxReTx_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CfmFcipEntityExtTcpMaxReTx_Type.__name__=_D
_CfmFcipEntityExtTcpMaxReTx_Object=MibTableColumn
cfmFcipEntityExtTcpMaxReTx=_CfmFcipEntityExtTcpMaxReTx_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,2),_CfmFcipEntityExtTcpMaxReTx_Type())
cfmFcipEntityExtTcpMaxReTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMaxReTx.setStatus(_B)
class _CfmFcipEntityExtPMTUEnable_Type(TruthValue):defaultValue=1
_CfmFcipEntityExtPMTUEnable_Type.__name__=_E
_CfmFcipEntityExtPMTUEnable_Object=MibTableColumn
cfmFcipEntityExtPMTUEnable=_CfmFcipEntityExtPMTUEnable_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,3),_CfmFcipEntityExtPMTUEnable_Type())
cfmFcipEntityExtPMTUEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtPMTUEnable.setStatus(_B)
class _CfmFcipEntityExtPMTUResetTO_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_CfmFcipEntityExtPMTUResetTO_Type.__name__=_D
_CfmFcipEntityExtPMTUResetTO_Object=MibTableColumn
cfmFcipEntityExtPMTUResetTO=_CfmFcipEntityExtPMTUResetTO_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,4),_CfmFcipEntityExtPMTUResetTO_Type())
cfmFcipEntityExtPMTUResetTO.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtPMTUResetTO.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtPMTUResetTO.setUnits(_U)
class _CfmFcipEntityExtTcpMinRTO_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_CfmFcipEntityExtTcpMinRTO_Type.__name__=_D
_CfmFcipEntityExtTcpMinRTO_Object=MibTableColumn
cfmFcipEntityExtTcpMinRTO=_CfmFcipEntityExtTcpMinRTO_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,5),_CfmFcipEntityExtTcpMinRTO_Type())
cfmFcipEntityExtTcpMinRTO.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMinRTO.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMinRTO.setUnits(_O)
class _CfmFcipEntityExtTcpSendBufSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_CfmFcipEntityExtTcpSendBufSize_Type.__name__=_D
_CfmFcipEntityExtTcpSendBufSize_Object=MibTableColumn
cfmFcipEntityExtTcpSendBufSize=_CfmFcipEntityExtTcpSendBufSize_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,6),_CfmFcipEntityExtTcpSendBufSize_Type())
cfmFcipEntityExtTcpSendBufSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpSendBufSize.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpSendBufSize.setUnits(_V)
class _CfmFcipEntityExtTcpMaxBW_Type(Unsigned32):defaultValue=1000000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,1000000))
_CfmFcipEntityExtTcpMaxBW_Type.__name__=_D
_CfmFcipEntityExtTcpMaxBW_Object=MibTableColumn
cfmFcipEntityExtTcpMaxBW=_CfmFcipEntityExtTcpMaxBW_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,7),_CfmFcipEntityExtTcpMaxBW_Type())
cfmFcipEntityExtTcpMaxBW.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMaxBW.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMaxBW.setUnits(_W)
class _CfmFcipEntityExtTcpMinAvailBW_Type(Unsigned32):defaultValue=15000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,1000000))
_CfmFcipEntityExtTcpMinAvailBW_Type.__name__=_D
_CfmFcipEntityExtTcpMinAvailBW_Object=MibTableColumn
cfmFcipEntityExtTcpMinAvailBW=_CfmFcipEntityExtTcpMinAvailBW_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,8),_CfmFcipEntityExtTcpMinAvailBW_Type())
cfmFcipEntityExtTcpMinAvailBW.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMinAvailBW.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMinAvailBW.setUnits(_W)
class _CfmFcipEntityExtTcpRndTrpTimeEst_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300000))
_CfmFcipEntityExtTcpRndTrpTimeEst_Type.__name__=_D
_CfmFcipEntityExtTcpRndTrpTimeEst_Object=MibTableColumn
cfmFcipEntityExtTcpRndTrpTimeEst=_CfmFcipEntityExtTcpRndTrpTimeEst_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,9),_CfmFcipEntityExtTcpRndTrpTimeEst_Type())
cfmFcipEntityExtTcpRndTrpTimeEst.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpRndTrpTimeEst.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpRndTrpTimeEst.setUnits('microseconds')
class _CfmFcipEntityExtCWMEnable_Type(TruthValue):defaultValue=1
_CfmFcipEntityExtCWMEnable_Type.__name__=_E
_CfmFcipEntityExtCWMEnable_Object=MibTableColumn
cfmFcipEntityExtCWMEnable=_CfmFcipEntityExtCWMEnable_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,10),_CfmFcipEntityExtCWMEnable_Type())
cfmFcipEntityExtCWMEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtCWMEnable.setStatus(_B)
class _CfmFcipEntityExtCWMBurstSize_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_CfmFcipEntityExtCWMBurstSize_Type.__name__=_D
_CfmFcipEntityExtCWMBurstSize_Object=MibTableColumn
cfmFcipEntityExtCWMBurstSize=_CfmFcipEntityExtCWMBurstSize_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,11),_CfmFcipEntityExtCWMBurstSize_Type())
cfmFcipEntityExtCWMBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtCWMBurstSize.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtCWMBurstSize.setUnits(_V)
_CfmFcipEntityExtTcpSACKEnable_Type=TruthValue
_CfmFcipEntityExtTcpSACKEnable_Object=MibTableColumn
cfmFcipEntityExtTcpSACKEnable=_CfmFcipEntityExtTcpSACKEnable_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,12),_CfmFcipEntityExtTcpSACKEnable_Type())
cfmFcipEntityExtTcpSACKEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpSACKEnable.setStatus(_B)
_CfmFcipEntityExtTcpLocalPort_Type=InetPortNumber
_CfmFcipEntityExtTcpLocalPort_Object=MibTableColumn
cfmFcipEntityExtTcpLocalPort=_CfmFcipEntityExtTcpLocalPort_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,13),_CfmFcipEntityExtTcpLocalPort_Type())
cfmFcipEntityExtTcpLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpLocalPort.setStatus(_B)
class _CfmFcipEntityExtTcpMaxJitter_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CfmFcipEntityExtTcpMaxJitter_Type.__name__=_D
_CfmFcipEntityExtTcpMaxJitter_Object=MibTableColumn
cfmFcipEntityExtTcpMaxJitter=_CfmFcipEntityExtTcpMaxJitter_Object((1,3,6,1,4,1,9,9,329,1,1,1,1,14),_CfmFcipEntityExtTcpMaxJitter_Type())
cfmFcipEntityExtTcpMaxJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMaxJitter.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipEntityExtTcpMaxJitter.setUnits(_O)
_CfmFcipLinkExtTable_Object=MibTable
cfmFcipLinkExtTable=_CfmFcipLinkExtTable_Object((1,3,6,1,4,1,9,9,329,1,1,2))
if mibBuilder.loadTexts:cfmFcipLinkExtTable.setStatus(_B)
_CfmFcipLinkExtEntry_Object=MibTableRow
cfmFcipLinkExtEntry=_CfmFcipLinkExtEntry_Object((1,3,6,1,4,1,9,9,329,1,1,2,1))
if mibBuilder.loadTexts:cfmFcipLinkExtEntry.setStatus(_B)
class _CfmFcipLinkExtPassiveMode_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtPassiveMode_Type.__name__=_E
_CfmFcipLinkExtPassiveMode_Object=MibTableColumn
cfmFcipLinkExtPassiveMode=_CfmFcipLinkExtPassiveMode_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,1),_CfmFcipLinkExtPassiveMode_Type())
cfmFcipLinkExtPassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtPassiveMode.setStatus(_B)
class _CfmFcipLinkExtNumTcpConn_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CfmFcipLinkExtNumTcpConn_Type.__name__=_D
_CfmFcipLinkExtNumTcpConn_Object=MibTableColumn
cfmFcipLinkExtNumTcpConn=_CfmFcipLinkExtNumTcpConn_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,2),_CfmFcipLinkExtNumTcpConn_Type())
cfmFcipLinkExtNumTcpConn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtNumTcpConn.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipLinkExtNumTcpConn.setUnits('tcp connections')
class _CfmFcipLinkExtCheckTimestamp_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtCheckTimestamp_Type.__name__=_E
_CfmFcipLinkExtCheckTimestamp_Object=MibTableColumn
cfmFcipLinkExtCheckTimestamp=_CfmFcipLinkExtCheckTimestamp_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,3),_CfmFcipLinkExtCheckTimestamp_Type())
cfmFcipLinkExtCheckTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtCheckTimestamp.setStatus(_B)
class _CfmFcipLinkExtTimestampTolerance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_CfmFcipLinkExtTimestampTolerance_Type.__name__=_D
_CfmFcipLinkExtTimestampTolerance_Object=MibTableColumn
cfmFcipLinkExtTimestampTolerance=_CfmFcipLinkExtTimestampTolerance_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,4),_CfmFcipLinkExtTimestampTolerance_Type())
cfmFcipLinkExtTimestampTolerance.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtTimestampTolerance.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipLinkExtTimestampTolerance.setUnits(_O)
class _CfmFcipLinkExtTcpRemPort_Type(CiscoPort):subtypeSpec=CiscoPort.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CfmFcipLinkExtTcpRemPort_Type.__name__=_S
_CfmFcipLinkExtTcpRemPort_Object=MibTableColumn
cfmFcipLinkExtTcpRemPort=_CfmFcipLinkExtTcpRemPort_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,5),_CfmFcipLinkExtTcpRemPort_Type())
cfmFcipLinkExtTcpRemPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtTcpRemPort.setStatus(_B)
class _CfmFcipLinkExtLocalBPortEnable_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtLocalBPortEnable_Type.__name__=_E
_CfmFcipLinkExtLocalBPortEnable_Object=MibTableColumn
cfmFcipLinkExtLocalBPortEnable=_CfmFcipLinkExtLocalBPortEnable_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,6),_CfmFcipLinkExtLocalBPortEnable_Type())
cfmFcipLinkExtLocalBPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtLocalBPortEnable.setStatus(_B)
class _CfmFcipLinkExtSpecialFrameEnable_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtSpecialFrameEnable_Type.__name__=_E
_CfmFcipLinkExtSpecialFrameEnable_Object=MibTableColumn
cfmFcipLinkExtSpecialFrameEnable=_CfmFcipLinkExtSpecialFrameEnable_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,7),_CfmFcipLinkExtSpecialFrameEnable_Type())
cfmFcipLinkExtSpecialFrameEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtSpecialFrameEnable.setStatus(_B)
class _CfmFcipLinkExtBPortKAEnable_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtBPortKAEnable_Type.__name__=_E
_CfmFcipLinkExtBPortKAEnable_Object=MibTableColumn
cfmFcipLinkExtBPortKAEnable=_CfmFcipLinkExtBPortKAEnable_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,8),_CfmFcipLinkExtBPortKAEnable_Type())
cfmFcipLinkExtBPortKAEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtBPortKAEnable.setStatus(_B)
class _CfmFcipLinkExtCntrlQOSField_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CfmFcipLinkExtCntrlQOSField_Type.__name__=_D
_CfmFcipLinkExtCntrlQOSField_Object=MibTableColumn
cfmFcipLinkExtCntrlQOSField=_CfmFcipLinkExtCntrlQOSField_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,9),_CfmFcipLinkExtCntrlQOSField_Type())
cfmFcipLinkExtCntrlQOSField.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtCntrlQOSField.setStatus(_B)
class _CfmFcipLinkExtDataQOSField_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CfmFcipLinkExtDataQOSField_Type.__name__=_D
_CfmFcipLinkExtDataQOSField_Object=MibTableColumn
cfmFcipLinkExtDataQOSField=_CfmFcipLinkExtDataQOSField_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,10),_CfmFcipLinkExtDataQOSField_Type())
cfmFcipLinkExtDataQOSField.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtDataQOSField.setStatus(_B)
_CfmFcipLinkExtEthIfIndex_Type=InterfaceIndex
_CfmFcipLinkExtEthIfIndex_Object=MibTableColumn
cfmFcipLinkExtEthIfIndex=_CfmFcipLinkExtEthIfIndex_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,11),_CfmFcipLinkExtEthIfIndex_Type())
cfmFcipLinkExtEthIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkExtEthIfIndex.setStatus(_B)
class _CfmFcipLinkExtWriteAccelerator_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtWriteAccelerator_Type.__name__=_E
_CfmFcipLinkExtWriteAccelerator_Object=MibTableColumn
cfmFcipLinkExtWriteAccelerator=_CfmFcipLinkExtWriteAccelerator_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,12),_CfmFcipLinkExtWriteAccelerator_Type())
cfmFcipLinkExtWriteAccelerator.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtWriteAccelerator.setStatus(_B)
class _CfmFcipLinkExtIPComp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('highCompressionRatio',2),('highThroughput',3),('auto',4),('mode1',5),('mode2',6),('mode3',7)))
_CfmFcipLinkExtIPComp_Type.__name__=_T
_CfmFcipLinkExtIPComp_Object=MibTableColumn
cfmFcipLinkExtIPComp=_CfmFcipLinkExtIPComp_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,13),_CfmFcipLinkExtIPComp_Type())
cfmFcipLinkExtIPComp.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtIPComp.setStatus(_B)
class _CfmFcipLinkExtTapeAccelerator_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtTapeAccelerator_Type.__name__=_E
_CfmFcipLinkExtTapeAccelerator_Object=MibTableColumn
cfmFcipLinkExtTapeAccelerator=_CfmFcipLinkExtTapeAccelerator_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,14),_CfmFcipLinkExtTapeAccelerator_Type())
cfmFcipLinkExtTapeAccelerator.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtTapeAccelerator.setStatus(_B)
class _CfmFcipLinkExtFlowCtrlBufSize_Type(Unsigned32):defaultValue=256;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12288))
_CfmFcipLinkExtFlowCtrlBufSize_Type.__name__=_D
_CfmFcipLinkExtFlowCtrlBufSize_Object=MibTableColumn
cfmFcipLinkExtFlowCtrlBufSize=_CfmFcipLinkExtFlowCtrlBufSize_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,15),_CfmFcipLinkExtFlowCtrlBufSize_Type())
cfmFcipLinkExtFlowCtrlBufSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtFlowCtrlBufSize.setStatus(_B)
if mibBuilder.loadTexts:cfmFcipLinkExtFlowCtrlBufSize.setUnits('bytes')
class _CfmFcipLinkExtIPSec_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtIPSec_Type.__name__=_E
_CfmFcipLinkExtIPSec_Object=MibTableColumn
cfmFcipLinkExtIPSec=_CfmFcipLinkExtIPSec_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,16),_CfmFcipLinkExtIPSec_Type())
cfmFcipLinkExtIPSec.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkExtIPSec.setStatus(_B)
_CfmFcipLinkExtPhyIfIndex_Type=InterfaceIndex
_CfmFcipLinkExtPhyIfIndex_Object=MibTableColumn
cfmFcipLinkExtPhyIfIndex=_CfmFcipLinkExtPhyIfIndex_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,17),_CfmFcipLinkExtPhyIfIndex_Type())
cfmFcipLinkExtPhyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkExtPhyIfIndex.setStatus(_B)
class _CfmFcipLinkExtWriteAccOper_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtWriteAccOper_Type.__name__=_E
_CfmFcipLinkExtWriteAccOper_Object=MibTableColumn
cfmFcipLinkExtWriteAccOper=_CfmFcipLinkExtWriteAccOper_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,18),_CfmFcipLinkExtWriteAccOper_Type())
cfmFcipLinkExtWriteAccOper.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkExtWriteAccOper.setStatus(_B)
class _CfmFcipLinkExtTapeAccOper_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtTapeAccOper_Type.__name__=_E
_CfmFcipLinkExtTapeAccOper_Object=MibTableColumn
cfmFcipLinkExtTapeAccOper=_CfmFcipLinkExtTapeAccOper_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,19),_CfmFcipLinkExtTapeAccOper_Type())
cfmFcipLinkExtTapeAccOper.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkExtTapeAccOper.setStatus(_B)
class _CfmFcipLinkExtTapeReadAccOper_Type(TruthValue):defaultValue=2
_CfmFcipLinkExtTapeReadAccOper_Type.__name__=_E
_CfmFcipLinkExtTapeReadAccOper_Object=MibTableColumn
cfmFcipLinkExtTapeReadAccOper=_CfmFcipLinkExtTapeReadAccOper_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,20),_CfmFcipLinkExtTapeReadAccOper_Type())
cfmFcipLinkExtTapeReadAccOper.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkExtTapeReadAccOper.setStatus(_B)
class _CfmFcipLinkExtFiconTAVsanL2k_Type(FcList):defaultHexValue=''
_CfmFcipLinkExtFiconTAVsanL2k_Type.__name__=_N
_CfmFcipLinkExtFiconTAVsanL2k_Object=MibTableColumn
cfmFcipLinkExtFiconTAVsanL2k=_CfmFcipLinkExtFiconTAVsanL2k_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,21),_CfmFcipLinkExtFiconTAVsanL2k_Type())
cfmFcipLinkExtFiconTAVsanL2k.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtFiconTAVsanL2k.setStatus(_B)
class _CfmFcipLinkExtFiconTAVsanL4k_Type(FcList):defaultHexValue=''
_CfmFcipLinkExtFiconTAVsanL4k_Type.__name__=_N
_CfmFcipLinkExtFiconTAVsanL4k_Object=MibTableColumn
cfmFcipLinkExtFiconTAVsanL4k=_CfmFcipLinkExtFiconTAVsanL4k_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,22),_CfmFcipLinkExtFiconTAVsanL4k_Type())
cfmFcipLinkExtFiconTAVsanL4k.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFcipLinkExtFiconTAVsanL4k.setStatus(_B)
_CfmFcipLinkExtFiconTAVsanLOper2k_Type=FcList
_CfmFcipLinkExtFiconTAVsanLOper2k_Object=MibTableColumn
cfmFcipLinkExtFiconTAVsanLOper2k=_CfmFcipLinkExtFiconTAVsanLOper2k_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,23),_CfmFcipLinkExtFiconTAVsanLOper2k_Type())
cfmFcipLinkExtFiconTAVsanLOper2k.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkExtFiconTAVsanLOper2k.setStatus(_B)
_CfmFcipLinkExtFiconTAVsanLOper4k_Type=FcList
_CfmFcipLinkExtFiconTAVsanLOper4k_Object=MibTableColumn
cfmFcipLinkExtFiconTAVsanLOper4k=_CfmFcipLinkExtFiconTAVsanLOper4k_Object((1,3,6,1,4,1,9,9,329,1,1,2,1,24),_CfmFcipLinkExtFiconTAVsanLOper4k_Type())
cfmFcipLinkExtFiconTAVsanLOper4k.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkExtFiconTAVsanLOper4k.setStatus(_B)
_CfmFcipLinkMapTable_Object=MibTable
cfmFcipLinkMapTable=_CfmFcipLinkMapTable_Object((1,3,6,1,4,1,9,9,329,1,1,3))
if mibBuilder.loadTexts:cfmFcipLinkMapTable.setStatus(_B)
_CfmFcipLinkMapEntry_Object=MibTableRow
cfmFcipLinkMapEntry=_CfmFcipLinkMapEntry_Object((1,3,6,1,4,1,9,9,329,1,1,3,1))
cfmFcipLinkMapEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:cfmFcipLinkMapEntry.setStatus(_B)
_CfmFcipLinkMapIndex_Type=Unsigned32
_CfmFcipLinkMapIndex_Object=MibTableColumn
cfmFcipLinkMapIndex=_CfmFcipLinkMapIndex_Object((1,3,6,1,4,1,9,9,329,1,1,3,1,1),_CfmFcipLinkMapIndex_Type())
cfmFcipLinkMapIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfmFcipLinkMapIndex.setStatus(_B)
_CfmFcipMapEntityId_Type=Unsigned32
_CfmFcipMapEntityId_Object=MibTableColumn
cfmFcipMapEntityId=_CfmFcipMapEntityId_Object((1,3,6,1,4,1,9,9,329,1,1,3,1,2),_CfmFcipMapEntityId_Type())
cfmFcipMapEntityId.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipMapEntityId.setStatus(_B)
_CfmFcipMgmtExtStats_ObjectIdentity=ObjectIdentity
cfmFcipMgmtExtStats=_CfmFcipMgmtExtStats_ObjectIdentity((1,3,6,1,4,1,9,9,329,1,2))
_CfmFcipLinkExtStatsTable_Object=MibTable
cfmFcipLinkExtStatsTable=_CfmFcipLinkExtStatsTable_Object((1,3,6,1,4,1,9,9,329,1,2,1))
if mibBuilder.loadTexts:cfmFcipLinkExtStatsTable.setStatus(_B)
_CfmFcipLinkExtStatsEntry_Object=MibTableRow
cfmFcipLinkExtStatsEntry=_CfmFcipLinkExtStatsEntry_Object((1,3,6,1,4,1,9,9,329,1,2,1,1))
if mibBuilder.loadTexts:cfmFcipLinkExtStatsEntry.setStatus(_B)
_CfmFcipLinkStatsRxIPCompRatio_Type=SnmpAdminString
_CfmFcipLinkStatsRxIPCompRatio_Object=MibTableColumn
cfmFcipLinkStatsRxIPCompRatio=_CfmFcipLinkStatsRxIPCompRatio_Object((1,3,6,1,4,1,9,9,329,1,2,1,1,1),_CfmFcipLinkStatsRxIPCompRatio_Type())
cfmFcipLinkStatsRxIPCompRatio.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkStatsRxIPCompRatio.setStatus(_B)
_CfmFcipLinkStatsTxIPCompRatio_Type=SnmpAdminString
_CfmFcipLinkStatsTxIPCompRatio_Object=MibTableColumn
cfmFcipLinkStatsTxIPCompRatio=_CfmFcipLinkStatsTxIPCompRatio_Object((1,3,6,1,4,1,9,9,329,1,2,1,1,2),_CfmFcipLinkStatsTxIPCompRatio_Type())
cfmFcipLinkStatsTxIPCompRatio.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmFcipLinkStatsTxIPCompRatio.setStatus(_B)
_CiscoFcipMgmtExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoFcipMgmtExtMIBConform=_CiscoFcipMgmtExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,329,2))
_CfmFcipExtCompliances_ObjectIdentity=ObjectIdentity
cfmFcipExtCompliances=_CfmFcipExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,329,2,1))
_CfmFcipExtGroups_ObjectIdentity=ObjectIdentity
cfmFcipExtGroups=_CfmFcipExtGroups_ObjectIdentity((1,3,6,1,4,1,9,9,329,2,2))
cfmFcipEntityInstanceEntry.registerAugmentions((_A,_Y))
cfmFcipEntityExtEntry.setIndexNames(*cfmFcipEntityInstanceEntry.getIndexNames())
cfmFcipLinkEntry.registerAugmentions((_A,_Z))
cfmFcipLinkExtEntry.setIndexNames(*cfmFcipLinkEntry.getIndexNames())
cfmFcipLinkEntry.registerAugmentions((_A,_a))
cfmFcipLinkExtStatsEntry.setIndexNames(*cfmFcipLinkEntry.getIndexNames())
cfmFcipEntityExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,1))
cfmFcipEntityExtGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:cfmFcipEntityExtGroup.setStatus(_B)
cfmFcipLinkExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,2))
cfmFcipLinkExtGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:cfmFcipLinkExtGroup.setStatus(_B)
cfmFcipLinkExtGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,3))
cfmFcipLinkExtGroupRev1.setObjects(*((_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cfmFcipLinkExtGroupRev1.setStatus(_B)
cfmFcipEntityExtCWMGroup=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,4))
cfmFcipEntityExtCWMGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:cfmFcipEntityExtCWMGroup.setStatus(_B)
cfmFcipLinkExtGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,5))
cfmFcipLinkExtGroupRev2.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:cfmFcipLinkExtGroupRev2.setStatus(_B)
cfmFcipLinkExtMapGroup=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,6))
cfmFcipLinkExtMapGroup.setObjects((_A,_A3))
if mibBuilder.loadTexts:cfmFcipLinkExtMapGroup.setStatus(_B)
cfmFcipEntityExtGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,7))
cfmFcipEntityExtGroupSup1.setObjects((_A,_A4))
if mibBuilder.loadTexts:cfmFcipEntityExtGroupSup1.setStatus(_B)
cfmFcipLinkExtGroupRev2Sup1=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,8))
cfmFcipLinkExtGroupRev2Sup1.setObjects((_A,_A5))
if mibBuilder.loadTexts:cfmFcipLinkExtGroupRev2Sup1.setStatus(_B)
cfmFcipLinkExtGroupRev2Sup2=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,9))
cfmFcipLinkExtGroupRev2Sup2.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:cfmFcipLinkExtGroupRev2Sup2.setStatus(_B)
cfmFcipLinkExtStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,10))
cfmFcipLinkExtStatsGroup.setObjects(*((_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:cfmFcipLinkExtStatsGroup.setStatus(_B)
cfmFcipLinkExtGroupRev2Sup3=ObjectGroup((1,3,6,1,4,1,9,9,329,2,2,11))
cfmFcipLinkExtGroupRev2Sup3.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:cfmFcipLinkExtGroupRev2Sup3.setStatus(_B)
cfmFcipExtCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,329,2,1,1))
cfmFcipExtCompliance.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cfmFcipExtCompliance.setStatus(_J)
cfmFcipExtCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,329,2,1,2))
cfmFcipExtCompliance1.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:cfmFcipExtCompliance1.setStatus(_J)
cfmFcipExtCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,329,2,1,3))
cfmFcipExtCompliance2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:cfmFcipExtCompliance2.setStatus(_J)
cfmFcipExtCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,329,2,1,4))
cfmFcipExtCompliance3.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_K),(_A,_L),(_A,_P)))
if mibBuilder.loadTexts:cfmFcipExtCompliance3.setStatus(_J)
cfmFcipExtCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,329,2,1,5))
cfmFcipExtCompliance4.setObjects(*((_A,_G),(_A,_AG),(_A,_H),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:cfmFcipExtCompliance4.setStatus(_J)
cfmFcipExtCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,329,2,1,6))
cfmFcipExtCompliance5.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cfmFcipExtCompliance5.setStatus(_J)
cfmFcipExtCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,329,2,1,7))
cfmFcipExtCompliance6.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R),(_A,_AH)))
if mibBuilder.loadTexts:cfmFcipExtCompliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoFcipMgmtExtMIB':ciscoFcipMgmtExtMIB,'ciscoFcipMgmtExtMIBNotifs':ciscoFcipMgmtExtMIBNotifs,'ciscoFcipMgmtExtMIBObjects':ciscoFcipMgmtExtMIBObjects,'cfmFcipMgmtExtConfig':cfmFcipMgmtExtConfig,'cfmFcipEntityExtTable':cfmFcipEntityExtTable,_Y:cfmFcipEntityExtEntry,_b:cfmFcipEntityExtTcpKeepAliveTO,_c:cfmFcipEntityExtTcpMaxReTx,_d:cfmFcipEntityExtPMTUEnable,_e:cfmFcipEntityExtPMTUResetTO,_f:cfmFcipEntityExtTcpMinRTO,_g:cfmFcipEntityExtTcpSendBufSize,_h:cfmFcipEntityExtTcpMaxBW,_i:cfmFcipEntityExtTcpMinAvailBW,_j:cfmFcipEntityExtTcpRndTrpTimeEst,_x:cfmFcipEntityExtCWMEnable,_y:cfmFcipEntityExtCWMBurstSize,_z:cfmFcipEntityExtTcpSACKEnable,_A0:cfmFcipEntityExtTcpLocalPort,_A4:cfmFcipEntityExtTcpMaxJitter,'cfmFcipLinkExtTable':cfmFcipLinkExtTable,_Z:cfmFcipLinkExtEntry,_k:cfmFcipLinkExtPassiveMode,_l:cfmFcipLinkExtNumTcpConn,_m:cfmFcipLinkExtCheckTimestamp,_n:cfmFcipLinkExtTimestampTolerance,_o:cfmFcipLinkExtTcpRemPort,_p:cfmFcipLinkExtLocalBPortEnable,_q:cfmFcipLinkExtSpecialFrameEnable,_r:cfmFcipLinkExtBPortKAEnable,_s:cfmFcipLinkExtCntrlQOSField,_t:cfmFcipLinkExtDataQOSField,_u:cfmFcipLinkExtEthIfIndex,_v:cfmFcipLinkExtWriteAccelerator,_w:cfmFcipLinkExtIPComp,_A1:cfmFcipLinkExtTapeAccelerator,_A2:cfmFcipLinkExtFlowCtrlBufSize,_A5:cfmFcipLinkExtIPSec,_A6:cfmFcipLinkExtPhyIfIndex,_A7:cfmFcipLinkExtWriteAccOper,_A8:cfmFcipLinkExtTapeAccOper,_AB:cfmFcipLinkExtTapeReadAccOper,_AC:cfmFcipLinkExtFiconTAVsanL2k,_AD:cfmFcipLinkExtFiconTAVsanL4k,_AE:cfmFcipLinkExtFiconTAVsanLOper2k,_AF:cfmFcipLinkExtFiconTAVsanLOper4k,'cfmFcipLinkMapTable':cfmFcipLinkMapTable,'cfmFcipLinkMapEntry':cfmFcipLinkMapEntry,_X:cfmFcipLinkMapIndex,_A3:cfmFcipMapEntityId,'cfmFcipMgmtExtStats':cfmFcipMgmtExtStats,'cfmFcipLinkExtStatsTable':cfmFcipLinkExtStatsTable,_a:cfmFcipLinkExtStatsEntry,_A9:cfmFcipLinkStatsRxIPCompRatio,_AA:cfmFcipLinkStatsTxIPCompRatio,'ciscoFcipMgmtExtMIBConform':ciscoFcipMgmtExtMIBConform,'cfmFcipExtCompliances':cfmFcipExtCompliances,'cfmFcipExtCompliance':cfmFcipExtCompliance,'cfmFcipExtCompliance1':cfmFcipExtCompliance1,'cfmFcipExtCompliance2':cfmFcipExtCompliance2,'cfmFcipExtCompliance3':cfmFcipExtCompliance3,'cfmFcipExtCompliance4':cfmFcipExtCompliance4,'cfmFcipExtCompliance5':cfmFcipExtCompliance5,'cfmFcipExtCompliance6':cfmFcipExtCompliance6,'cfmFcipExtGroups':cfmFcipExtGroups,_G:cfmFcipEntityExtGroup,_H:cfmFcipLinkExtGroup,_I:cfmFcipLinkExtGroupRev1,_K:cfmFcipEntityExtCWMGroup,_L:cfmFcipLinkExtGroupRev2,_P:cfmFcipLinkExtMapGroup,_AG:cfmFcipEntityExtGroupSup1,_M:cfmFcipLinkExtGroupRev2Sup1,_Q:cfmFcipLinkExtGroupRev2Sup2,_R:cfmFcipLinkExtStatsGroup,_AH:cfmFcipLinkExtGroupRev2Sup3})