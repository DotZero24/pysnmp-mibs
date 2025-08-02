_AL='fwWAFProtectionGroup'
_AK='fwProxyObjectGroup'
_AJ='fwSystemObjectGroup'
_AI='fwTrapGroup'
_AH='fwTrapWAFWListAttack'
_AG='fwTrapWAFSignatureAttack'
_AF='fwTrapWAFBadRobotAttack'
_AE='fwTrapWAFUrlAccessAttack'
_AD='fwTrapWAFHideFieldAttack'
_AC='fwTrapWAFRobotAttack'
_AB='fwTrapWAFBLoginAttack'
_AA='fwTrapWAFBListAttack'
_A9='fwTrapWAFPValidAttack'
_A8='fwTrapWAFSPageAttack'
_A7='fwTrapWAFAccessAttack'
_A6='fwTrapWAFDisclosureAttack'
_A5='fwTrapWAFExploitAttack'
_A4='fwTrapWAFSqlAttack'
_A3='fwTrapWAFXSSAttack'
_A2='fwTrapWAFAMethodAttack'
_A1='fwTrapXMLSqlAttack'
_A0='fwTrapXMLWSDLAttack'
_z='fwTrapXMLSigEncAttack'
_y='fwTrapXMLFilterAttack'
_x='fwTrapXMLSchemaAttack'
_w='fwTrapXMLIntrusionAttack'
_v='fwTrapHAMemberLeave'
_u='fwTrapHAMemberJoin'
_t='fwTrapHAStatusChange'
_s='fwTrapPServerFailed'
_r='fwTrapPolicyStop'
_q='fwTrapPolicyStart'
_p='fwTrapModeChange'
_o='fwTrapHaHBFail'
_n='fwWAFProfileNumber'
_m='fwWAFSvrPortNumber'
_l='fwWAFParameterNumber'
_k='fwWAFInputRuleNumber'
_j='fwTotalConnectNumberPerSecond'
_i='fwTotalConnectNumber'
_h='fwPortSvrNumber'
_g='fwServiceNumber'
_f='fwMonitorNumber'
_e='fwVServerNumber'
_d='fwPServerNumber'
_c='fwProxyNumber'
_b='cPUusage'
_a='cPUNumber'
_Z='fwSysDiskCapacity'
_Y='fwSysDiskUsage'
_X='fwSysMemCapacity'
_W='fwSysMemUsage'
_V='fwSysCpuFreq'
_U='fwSysCpuUsage'
_T='fwSysOpMode'
_S='fwSysHaMode'
_R='fwSysVersion'
_Q='fwSysModel'
_P='fnWafIndex'
_O='not-accessible'
_N='cPUIndex'
_M='2018-08-06 00:00'
_L='DisplayString'
_K='Integer32'
_J='Gauge32'
_I='2020-07-02 00:00'
_H='fnWafInfoDetail'
_G='sysName'
_F='SNMPv2-MIB'
_E='fnSysSerial'
_D='FORTINET-CORE-MIB'
_C='read-only'
_B='FORTINET-FORTIWEB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fnSysSerial,fortinet=mibBuilder.importSymbols(_D,_E,'fortinet')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_J,_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
fnFortiWebMib=ModuleIdentity((1,3,6,1,4,1,12356,107))
if mibBuilder.loadTexts:fnFortiWebMib.setRevisions((_I,_I,_I,_I,_I,_I,'2019-08-15 00:00','2019-04-29 00:00','2018-09-20 00:00','2018-09-13 00:00',_M,_M,'2018-04-04 00:00','2018-03-21 00:00','2017-11-17 00:00','2017-02-13 00:00','2016-12-13 00:00','2016-10-25 00:00','2016-09-13 00:00','2016-07-01 00:00','2015-12-17 00:00','2015-12-16 00:00','2015-12-03 00:00','2015-10-20 00:00','2015-07-13 00:00','2010-03-22 00:00'))
class FwOpMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inline',1),('offline',2),('transparent',3),('wccp',4),('inspection',5)))
class FwHaMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standalone',1),('master',2),('slave',3)))
_FwModel_ObjectIdentity=ObjectIdentity
fwModel=_FwModel_ObjectIdentity((1,3,6,1,4,1,12356,107,1))
_Fwb100D_ObjectIdentity=ObjectIdentity
fwb100D=_Fwb100D_ObjectIdentity((1,3,6,1,4,1,12356,107,1,1004))
_Fwb100E_ObjectIdentity=ObjectIdentity
fwb100E=_Fwb100E_ObjectIdentity((1,3,6,1,4,1,12356,107,1,1005))
_Fwb400B_ObjectIdentity=ObjectIdentity
fwb400B=_Fwb400B_ObjectIdentity((1,3,6,1,4,1,12356,107,1,4002))
_Fwb400C_ObjectIdentity=ObjectIdentity
fwb400C=_Fwb400C_ObjectIdentity((1,3,6,1,4,1,12356,107,1,4003))
_Fwb400D_ObjectIdentity=ObjectIdentity
fwb400D=_Fwb400D_ObjectIdentity((1,3,6,1,4,1,12356,107,1,4004))
_Fwb400E_ObjectIdentity=ObjectIdentity
fwb400E=_Fwb400E_ObjectIdentity((1,3,6,1,4,1,12356,107,1,4005))
_Fwb600D_ObjectIdentity=ObjectIdentity
fwb600D=_Fwb600D_ObjectIdentity((1,3,6,1,4,1,12356,107,1,6004))
_Fwb600E_ObjectIdentity=ObjectIdentity
fwb600E=_Fwb600E_ObjectIdentity((1,3,6,1,4,1,12356,107,1,6005))
_Fwb1000B_ObjectIdentity=ObjectIdentity
fwb1000B=_Fwb1000B_ObjectIdentity((1,3,6,1,4,1,12356,107,1,10002))
_Fwb1000C_ObjectIdentity=ObjectIdentity
fwb1000C=_Fwb1000C_ObjectIdentity((1,3,6,1,4,1,12356,107,1,10003))
_Fwb1000D_ObjectIdentity=ObjectIdentity
fwb1000D=_Fwb1000D_ObjectIdentity((1,3,6,1,4,1,12356,107,1,10004))
_Fwb2000E_ObjectIdentity=ObjectIdentity
fwb2000E=_Fwb2000E_ObjectIdentity((1,3,6,1,4,1,12356,107,1,10005))
_Fwb1000E_ObjectIdentity=ObjectIdentity
fwb1000E=_Fwb1000E_ObjectIdentity((1,3,6,1,4,1,12356,107,1,10006))
_Fwb3000C_ObjectIdentity=ObjectIdentity
fwb3000C=_Fwb3000C_ObjectIdentity((1,3,6,1,4,1,12356,107,1,30003))
_Fwb3000CFSX_ObjectIdentity=ObjectIdentity
fwb3000CFSX=_Fwb3000CFSX_ObjectIdentity((1,3,6,1,4,1,12356,107,1,30004))
_Fwb3000D_ObjectIdentity=ObjectIdentity
fwb3000D=_Fwb3000D_ObjectIdentity((1,3,6,1,4,1,12356,107,1,30005))
_Fwb3000DFSX_ObjectIdentity=ObjectIdentity
fwb3000DFSX=_Fwb3000DFSX_ObjectIdentity((1,3,6,1,4,1,12356,107,1,30006))
_Fwb3000E_ObjectIdentity=ObjectIdentity
fwb3000E=_Fwb3000E_ObjectIdentity((1,3,6,1,4,1,12356,107,1,30007))
_Fwb3010E_ObjectIdentity=ObjectIdentity
fwb3010E=_Fwb3010E_ObjectIdentity((1,3,6,1,4,1,12356,107,1,30008))
_Fwb4000C_ObjectIdentity=ObjectIdentity
fwb4000C=_Fwb4000C_ObjectIdentity((1,3,6,1,4,1,12356,107,1,40003))
_Fwb4000D_ObjectIdentity=ObjectIdentity
fwb4000D=_Fwb4000D_ObjectIdentity((1,3,6,1,4,1,12356,107,1,40004))
_Fwb4000E_ObjectIdentity=ObjectIdentity
fwb4000E=_Fwb4000E_ObjectIdentity((1,3,6,1,4,1,12356,107,1,40005))
_FwbVM_ObjectIdentity=ObjectIdentity
fwbVM=_FwbVM_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50001))
_FwbXENOPEN_ObjectIdentity=ObjectIdentity
fwbXENOPEN=_FwbXENOPEN_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50002))
_FwbXENSERVER_ObjectIdentity=ObjectIdentity
fwbXENSERVER=_FwbXENSERVER_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50003))
_FwbXENAWS_ObjectIdentity=ObjectIdentity
fwbXENAWS=_FwbXENAWS_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50004))
_FwbHYPERV_ObjectIdentity=ObjectIdentity
fwbHYPERV=_FwbHYPERV_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50005))
_FwbKVM_ObjectIdentity=ObjectIdentity
fwbKVM=_FwbKVM_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50006))
_FwbAZURE_ObjectIdentity=ObjectIdentity
fwbAZURE=_FwbAZURE_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50007))
_FwbVMPAYG_ObjectIdentity=ObjectIdentity
fwbVMPAYG=_FwbVMPAYG_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50008))
_FwbKVMPAYG_ObjectIdentity=ObjectIdentity
fwbKVMPAYG=_FwbKVMPAYG_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50009))
_FwbGCP_ObjectIdentity=ObjectIdentity
fwbGCP=_FwbGCP_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50010))
_FwbVBOX_ObjectIdentity=ObjectIdentity
fwbVBOX=_FwbVBOX_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50011))
_FwbDOCKER_ObjectIdentity=ObjectIdentity
fwbDOCKER=_FwbDOCKER_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50012))
_FwbOCI_ObjectIdentity=ObjectIdentity
fwbOCI=_FwbOCI_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50013))
_FwbALI_ObjectIdentity=ObjectIdentity
fwbALI=_FwbALI_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50014))
_FwbAZRCLD_ObjectIdentity=ObjectIdentity
fwbAZRCLD=_FwbAZRCLD_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50015))
_FwbAZROND_ObjectIdentity=ObjectIdentity
fwbAZROND=_FwbAZROND_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50016))
_FwbXENAWSOND_ObjectIdentity=ObjectIdentity
fwbXENAWSOND=_FwbXENAWSOND_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50017))
_FwbAWSCLD_ObjectIdentity=ObjectIdentity
fwbAWSCLD=_FwbAWSCLD_ObjectIdentity((1,3,6,1,4,1,12356,107,1,50018))
_FwSystem_ObjectIdentity=ObjectIdentity
fwSystem=_FwSystem_ObjectIdentity((1,3,6,1,4,1,12356,107,2))
_FwSystemInfo_ObjectIdentity=ObjectIdentity
fwSystemInfo=_FwSystemInfo_ObjectIdentity((1,3,6,1,4,1,12356,107,2,1))
class _FwSysModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FwSysModel_Type.__name__=_L
_FwSysModel_Object=MibScalar
fwSysModel=_FwSysModel_Object((1,3,6,1,4,1,12356,107,2,1,1),_FwSysModel_Type())
fwSysModel.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysModel.setStatus(_A)
class _FwSysVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FwSysVersion_Type.__name__=_L
_FwSysVersion_Object=MibScalar
fwSysVersion=_FwSysVersion_Object((1,3,6,1,4,1,12356,107,2,1,2),_FwSysVersion_Type())
fwSysVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysVersion.setStatus(_A)
_FwSysHaMode_Type=FwHaMode
_FwSysHaMode_Object=MibScalar
fwSysHaMode=_FwSysHaMode_Object((1,3,6,1,4,1,12356,107,2,1,3),_FwSysHaMode_Type())
fwSysHaMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysHaMode.setStatus(_A)
_FwSysOpMode_Type=FwOpMode
_FwSysOpMode_Object=MibScalar
fwSysOpMode=_FwSysOpMode_Object((1,3,6,1,4,1,12356,107,2,1,4),_FwSysOpMode_Type())
fwSysOpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysOpMode.setStatus(_A)
class _FwSysCpuUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FwSysCpuUsage_Type.__name__=_J
_FwSysCpuUsage_Object=MibScalar
fwSysCpuUsage=_FwSysCpuUsage_Object((1,3,6,1,4,1,12356,107,2,1,5),_FwSysCpuUsage_Type())
fwSysCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysCpuUsage.setStatus(_A)
_FwSysCpuFreq_Type=Gauge32
_FwSysCpuFreq_Object=MibScalar
fwSysCpuFreq=_FwSysCpuFreq_Object((1,3,6,1,4,1,12356,107,2,1,6),_FwSysCpuFreq_Type())
fwSysCpuFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysCpuFreq.setStatus(_A)
class _FwSysMemUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FwSysMemUsage_Type.__name__=_J
_FwSysMemUsage_Object=MibScalar
fwSysMemUsage=_FwSysMemUsage_Object((1,3,6,1,4,1,12356,107,2,1,7),_FwSysMemUsage_Type())
fwSysMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysMemUsage.setStatus(_A)
_FwSysMemCapacity_Type=Gauge32
_FwSysMemCapacity_Object=MibScalar
fwSysMemCapacity=_FwSysMemCapacity_Object((1,3,6,1,4,1,12356,107,2,1,8),_FwSysMemCapacity_Type())
fwSysMemCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysMemCapacity.setStatus(_A)
_FwSysDiskUsage_Type=Gauge32
_FwSysDiskUsage_Object=MibScalar
fwSysDiskUsage=_FwSysDiskUsage_Object((1,3,6,1,4,1,12356,107,2,1,9),_FwSysDiskUsage_Type())
fwSysDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysDiskUsage.setStatus(_A)
_FwSysDiskCapacity_Type=Gauge32
_FwSysDiskCapacity_Object=MibScalar
fwSysDiskCapacity=_FwSysDiskCapacity_Object((1,3,6,1,4,1,12356,107,2,1,10),_FwSysDiskCapacity_Type())
fwSysDiskCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:fwSysDiskCapacity.setStatus(_A)
_FwSystemCPU_ObjectIdentity=ObjectIdentity
fwSystemCPU=_FwSystemCPU_ObjectIdentity((1,3,6,1,4,1,12356,107,2,2))
_CPUNumber_Type=Integer32
_CPUNumber_Object=MibScalar
cPUNumber=_CPUNumber_Object((1,3,6,1,4,1,12356,107,2,2,1),_CPUNumber_Type())
cPUNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cPUNumber.setStatus(_A)
_CPUTable_Object=MibTable
cPUTable=_CPUTable_Object((1,3,6,1,4,1,12356,107,2,2,2))
if mibBuilder.loadTexts:cPUTable.setStatus(_A)
_CPUEntry_Object=MibTableRow
cPUEntry=_CPUEntry_Object((1,3,6,1,4,1,12356,107,2,2,2,1))
cPUEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cPUEntry.setStatus(_A)
class _CPUIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CPUIndex_Type.__name__=_K
_CPUIndex_Object=MibTableColumn
cPUIndex=_CPUIndex_Object((1,3,6,1,4,1,12356,107,2,2,2,1,1),_CPUIndex_Type())
cPUIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:cPUIndex.setStatus(_A)
_CPUusage_Type=Integer32
_CPUusage_Object=MibTableColumn
cPUusage=_CPUusage_Object((1,3,6,1,4,1,12356,107,2,2,2,1,2),_CPUusage_Type())
cPUusage.setMaxAccess(_C)
if mibBuilder.loadTexts:cPUusage.setStatus(_A)
_FwProxy_ObjectIdentity=ObjectIdentity
fwProxy=_FwProxy_ObjectIdentity((1,3,6,1,4,1,12356,107,3))
_FwProxyNumber_Type=Gauge32
_FwProxyNumber_Object=MibScalar
fwProxyNumber=_FwProxyNumber_Object((1,3,6,1,4,1,12356,107,3,1),_FwProxyNumber_Type())
fwProxyNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwProxyNumber.setStatus(_A)
_FwPServerNumber_Type=Gauge32
_FwPServerNumber_Object=MibScalar
fwPServerNumber=_FwPServerNumber_Object((1,3,6,1,4,1,12356,107,3,2),_FwPServerNumber_Type())
fwPServerNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwPServerNumber.setStatus(_A)
_FwVServerNumber_Type=Gauge32
_FwVServerNumber_Object=MibScalar
fwVServerNumber=_FwVServerNumber_Object((1,3,6,1,4,1,12356,107,3,3),_FwVServerNumber_Type())
fwVServerNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwVServerNumber.setStatus(_A)
_FwMonitorNumber_Type=Gauge32
_FwMonitorNumber_Object=MibScalar
fwMonitorNumber=_FwMonitorNumber_Object((1,3,6,1,4,1,12356,107,3,4),_FwMonitorNumber_Type())
fwMonitorNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwMonitorNumber.setStatus(_A)
_FwServiceNumber_Type=Gauge32
_FwServiceNumber_Object=MibScalar
fwServiceNumber=_FwServiceNumber_Object((1,3,6,1,4,1,12356,107,3,5),_FwServiceNumber_Type())
fwServiceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwServiceNumber.setStatus(_A)
_FwPortSvrNumber_Type=Gauge32
_FwPortSvrNumber_Object=MibScalar
fwPortSvrNumber=_FwPortSvrNumber_Object((1,3,6,1,4,1,12356,107,3,6),_FwPortSvrNumber_Type())
fwPortSvrNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwPortSvrNumber.setStatus(_A)
_FwTotalConnectNumber_Type=Gauge32
_FwTotalConnectNumber_Object=MibScalar
fwTotalConnectNumber=_FwTotalConnectNumber_Object((1,3,6,1,4,1,12356,107,3,7),_FwTotalConnectNumber_Type())
fwTotalConnectNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwTotalConnectNumber.setStatus(_A)
_FwTotalConnectNumberPerSecond_Type=Gauge32
_FwTotalConnectNumberPerSecond_Object=MibScalar
fwTotalConnectNumberPerSecond=_FwTotalConnectNumberPerSecond_Object((1,3,6,1,4,1,12356,107,3,8),_FwTotalConnectNumberPerSecond_Type())
fwTotalConnectNumberPerSecond.setMaxAccess(_C)
if mibBuilder.loadTexts:fwTotalConnectNumberPerSecond.setStatus(_A)
_FwWAFProtection_ObjectIdentity=ObjectIdentity
fwWAFProtection=_FwWAFProtection_ObjectIdentity((1,3,6,1,4,1,12356,107,4))
_FwWAFInputRuleNumber_Type=Gauge32
_FwWAFInputRuleNumber_Object=MibScalar
fwWAFInputRuleNumber=_FwWAFInputRuleNumber_Object((1,3,6,1,4,1,12356,107,4,1),_FwWAFInputRuleNumber_Type())
fwWAFInputRuleNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwWAFInputRuleNumber.setStatus(_A)
_FwWAFParameterNumber_Type=Gauge32
_FwWAFParameterNumber_Object=MibScalar
fwWAFParameterNumber=_FwWAFParameterNumber_Object((1,3,6,1,4,1,12356,107,4,2),_FwWAFParameterNumber_Type())
fwWAFParameterNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwWAFParameterNumber.setStatus(_A)
_FwWAFSvrPortNumber_Type=Gauge32
_FwWAFSvrPortNumber_Object=MibScalar
fwWAFSvrPortNumber=_FwWAFSvrPortNumber_Object((1,3,6,1,4,1,12356,107,4,3),_FwWAFSvrPortNumber_Type())
fwWAFSvrPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwWAFSvrPortNumber.setStatus(_A)
_FwWAFProfileNumber_Type=Gauge32
_FwWAFProfileNumber_Object=MibScalar
fwWAFProfileNumber=_FwWAFProfileNumber_Object((1,3,6,1,4,1,12356,107,4,4),_FwWAFProfileNumber_Type())
fwWAFProfileNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fwWAFProfileNumber.setStatus(_A)
_FwTraps_ObjectIdentity=ObjectIdentity
fwTraps=_FwTraps_ObjectIdentity((1,3,6,1,4,1,12356,107,10))
_FwTrapPrefix_ObjectIdentity=ObjectIdentity
fwTrapPrefix=_FwTrapPrefix_ObjectIdentity((1,3,6,1,4,1,12356,107,10,0))
_FnWafInfo_Object=MibTable
fnWafInfo=_FnWafInfo_Object((1,3,6,1,4,1,12356,107,10,1))
if mibBuilder.loadTexts:fnWafInfo.setStatus(_A)
_FnWafInfoDetail_Object=MibTableRow
fnWafInfoDetail=_FnWafInfoDetail_Object((1,3,6,1,4,1,12356,107,10,1,1))
fnWafInfoDetail.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:fnWafInfoDetail.setStatus(_A)
class _FnWafIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FnWafIndex_Type.__name__=_K
_FnWafIndex_Object=MibTableColumn
fnWafIndex=_FnWafIndex_Object((1,3,6,1,4,1,12356,107,10,1,1,1),_FnWafIndex_Type())
fnWafIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:fnWafIndex.setStatus(_A)
_FnWafDate_Type=DisplayString
_FnWafDate_Object=MibTableColumn
fnWafDate=_FnWafDate_Object((1,3,6,1,4,1,12356,107,10,1,1,2),_FnWafDate_Type())
fnWafDate.setMaxAccess(_C)
if mibBuilder.loadTexts:fnWafDate.setStatus(_A)
_FnWafTime_Type=DisplayString
_FnWafTime_Object=MibTableColumn
fnWafTime=_FnWafTime_Object((1,3,6,1,4,1,12356,107,10,1,1,3),_FnWafTime_Type())
fnWafTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fnWafTime.setStatus(_A)
_FnWafSrcIP_Type=DisplayString
_FnWafSrcIP_Object=MibTableColumn
fnWafSrcIP=_FnWafSrcIP_Object((1,3,6,1,4,1,12356,107,10,1,1,4),_FnWafSrcIP_Type())
fnWafSrcIP.setMaxAccess(_C)
if mibBuilder.loadTexts:fnWafSrcIP.setStatus(_A)
_FnWafDstIP_Type=DisplayString
_FnWafDstIP_Object=MibTableColumn
fnWafDstIP=_FnWafDstIP_Object((1,3,6,1,4,1,12356,107,10,1,1,5),_FnWafDstIP_Type())
fnWafDstIP.setMaxAccess(_C)
if mibBuilder.loadTexts:fnWafDstIP.setStatus(_A)
_FnWafSrcPort_Type=DisplayString
_FnWafSrcPort_Object=MibTableColumn
fnWafSrcPort=_FnWafSrcPort_Object((1,3,6,1,4,1,12356,107,10,1,1,6),_FnWafSrcPort_Type())
fnWafSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fnWafSrcPort.setStatus(_A)
_FnWafDstPort_Type=DisplayString
_FnWafDstPort_Object=MibTableColumn
fnWafDstPort=_FnWafDstPort_Object((1,3,6,1,4,1,12356,107,10,1,1,7),_FnWafDstPort_Type())
fnWafDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fnWafDstPort.setStatus(_A)
_FnWafHost_Type=DisplayString
_FnWafHost_Object=MibTableColumn
fnWafHost=_FnWafHost_Object((1,3,6,1,4,1,12356,107,10,1,1,8),_FnWafHost_Type())
fnWafHost.setMaxAccess(_C)
if mibBuilder.loadTexts:fnWafHost.setStatus(_A)
_FnWafURL_Type=DisplayString
_FnWafURL_Object=MibTableColumn
fnWafURL=_FnWafURL_Object((1,3,6,1,4,1,12356,107,10,1,1,9),_FnWafURL_Type())
fnWafURL.setMaxAccess(_C)
if mibBuilder.loadTexts:fnWafURL.setStatus(_A)
_FwMibConformance_ObjectIdentity=ObjectIdentity
fwMibConformance=_FwMibConformance_ObjectIdentity((1,3,6,1,4,1,12356,107,100))
fwSystemObjectGroup=ObjectGroup((1,3,6,1,4,1,12356,107,100,2))
fwSystemObjectGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:fwSystemObjectGroup.setStatus(_A)
fwProxyObjectGroup=ObjectGroup((1,3,6,1,4,1,12356,107,100,3))
fwProxyObjectGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:fwProxyObjectGroup.setStatus(_A)
fwWAFProtectionGroup=ObjectGroup((1,3,6,1,4,1,12356,107,100,4))
fwWAFProtectionGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:fwWAFProtectionGroup.setStatus(_A)
fwTrapHaHBFail=NotificationType((1,3,6,1,4,1,12356,107,10,0,1))
fwTrapHaHBFail.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapHaHBFail.setStatus(_A)
fwTrapModeChange=NotificationType((1,3,6,1,4,1,12356,107,10,0,2))
fwTrapModeChange.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapModeChange.setStatus(_A)
fwTrapPolicyStart=NotificationType((1,3,6,1,4,1,12356,107,10,0,3))
fwTrapPolicyStart.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapPolicyStart.setStatus(_A)
fwTrapPolicyStop=NotificationType((1,3,6,1,4,1,12356,107,10,0,4))
fwTrapPolicyStop.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapPolicyStop.setStatus(_A)
fwTrapPServerFailed=NotificationType((1,3,6,1,4,1,12356,107,10,0,5))
fwTrapPServerFailed.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapPServerFailed.setStatus(_A)
fwTrapHAStatusChange=NotificationType((1,3,6,1,4,1,12356,107,10,0,6))
fwTrapHAStatusChange.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapHAStatusChange.setStatus(_A)
fwTrapHAMemberJoin=NotificationType((1,3,6,1,4,1,12356,107,10,0,7))
fwTrapHAMemberJoin.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapHAMemberJoin.setStatus(_A)
fwTrapHAMemberLeave=NotificationType((1,3,6,1,4,1,12356,107,10,0,8))
fwTrapHAMemberLeave.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapHAMemberLeave.setStatus(_A)
fwTrapXMLIntrusionAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,10))
fwTrapXMLIntrusionAttack.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapXMLIntrusionAttack.setStatus(_A)
fwTrapXMLSchemaAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,11))
fwTrapXMLSchemaAttack.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapXMLSchemaAttack.setStatus(_A)
fwTrapXMLFilterAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,12))
fwTrapXMLFilterAttack.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapXMLFilterAttack.setStatus(_A)
fwTrapXMLSigEncAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,13))
fwTrapXMLSigEncAttack.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapXMLSigEncAttack.setStatus(_A)
fwTrapXMLWSDLAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,14))
fwTrapXMLWSDLAttack.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapXMLWSDLAttack.setStatus(_A)
fwTrapXMLSqlAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,15))
fwTrapXMLSqlAttack.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapXMLSqlAttack.setStatus(_A)
fwTrapWAFAMethodAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,30))
fwTrapWAFAMethodAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFAMethodAttack.setStatus(_A)
fwTrapWAFXSSAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,31))
fwTrapWAFXSSAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFXSSAttack.setStatus(_A)
fwTrapWAFSqlAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,32))
fwTrapWAFSqlAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFSqlAttack.setStatus(_A)
fwTrapWAFExploitAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,33))
fwTrapWAFExploitAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFExploitAttack.setStatus(_A)
fwTrapWAFDisclosureAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,34))
fwTrapWAFDisclosureAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFDisclosureAttack.setStatus(_A)
fwTrapWAFAccessAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,35))
fwTrapWAFAccessAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFAccessAttack.setStatus(_A)
fwTrapWAFSPageAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,36))
fwTrapWAFSPageAttack.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapWAFSPageAttack.setStatus(_A)
fwTrapWAFPValidAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,37))
fwTrapWAFPValidAttack.setObjects(*((_D,_E),(_F,_G)))
if mibBuilder.loadTexts:fwTrapWAFPValidAttack.setStatus(_A)
fwTrapWAFBListAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,38))
fwTrapWAFBListAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFBListAttack.setStatus(_A)
fwTrapWAFBLoginAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,39))
fwTrapWAFBLoginAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFBLoginAttack.setStatus(_A)
fwTrapWAFRobotAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,40))
fwTrapWAFRobotAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFRobotAttack.setStatus(_A)
fwTrapWAFHideFieldAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,41))
fwTrapWAFHideFieldAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFHideFieldAttack.setStatus(_A)
fwTrapWAFUrlAccessAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,42))
fwTrapWAFUrlAccessAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFUrlAccessAttack.setStatus(_A)
fwTrapWAFBadRobotAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,43))
fwTrapWAFBadRobotAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFBadRobotAttack.setStatus(_A)
fwTrapWAFSignatureAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,44))
fwTrapWAFSignatureAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFSignatureAttack.setStatus(_A)
fwTrapWAFWListAttack=NotificationType((1,3,6,1,4,1,12356,107,10,0,45))
fwTrapWAFWListAttack.setObjects(*((_D,_E),(_F,_G),(_B,_H)))
if mibBuilder.loadTexts:fwTrapWAFWListAttack.setStatus(_A)
fwTrapGroup=NotificationGroup((1,3,6,1,4,1,12356,107,100,1))
fwTrapGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:fwTrapGroup.setStatus(_A)
fwMibCompliance=ModuleCompliance((1,3,6,1,4,1,12356,107,100,100))
fwMibCompliance.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:fwMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FwOpMode':FwOpMode,'FwHaMode':FwHaMode,'fnFortiWebMib':fnFortiWebMib,'fwModel':fwModel,'fwb100D':fwb100D,'fwb100E':fwb100E,'fwb400B':fwb400B,'fwb400C':fwb400C,'fwb400D':fwb400D,'fwb400E':fwb400E,'fwb600D':fwb600D,'fwb600E':fwb600E,'fwb1000B':fwb1000B,'fwb1000C':fwb1000C,'fwb1000D':fwb1000D,'fwb2000E':fwb2000E,'fwb1000E':fwb1000E,'fwb3000C':fwb3000C,'fwb3000CFSX':fwb3000CFSX,'fwb3000D':fwb3000D,'fwb3000DFSX':fwb3000DFSX,'fwb3000E':fwb3000E,'fwb3010E':fwb3010E,'fwb4000C':fwb4000C,'fwb4000D':fwb4000D,'fwb4000E':fwb4000E,'fwbVM':fwbVM,'fwbXENOPEN':fwbXENOPEN,'fwbXENSERVER':fwbXENSERVER,'fwbXENAWS':fwbXENAWS,'fwbHYPERV':fwbHYPERV,'fwbKVM':fwbKVM,'fwbAZURE':fwbAZURE,'fwbVMPAYG':fwbVMPAYG,'fwbKVMPAYG':fwbKVMPAYG,'fwbGCP':fwbGCP,'fwbVBOX':fwbVBOX,'fwbDOCKER':fwbDOCKER,'fwbOCI':fwbOCI,'fwbALI':fwbALI,'fwbAZRCLD':fwbAZRCLD,'fwbAZROND':fwbAZROND,'fwbXENAWSOND':fwbXENAWSOND,'fwbAWSCLD':fwbAWSCLD,'fwSystem':fwSystem,'fwSystemInfo':fwSystemInfo,_Q:fwSysModel,_R:fwSysVersion,_S:fwSysHaMode,_T:fwSysOpMode,_U:fwSysCpuUsage,_V:fwSysCpuFreq,_W:fwSysMemUsage,_X:fwSysMemCapacity,_Y:fwSysDiskUsage,_Z:fwSysDiskCapacity,'fwSystemCPU':fwSystemCPU,_a:cPUNumber,'cPUTable':cPUTable,'cPUEntry':cPUEntry,_N:cPUIndex,_b:cPUusage,'fwProxy':fwProxy,_c:fwProxyNumber,_d:fwPServerNumber,_e:fwVServerNumber,_f:fwMonitorNumber,_g:fwServiceNumber,_h:fwPortSvrNumber,_i:fwTotalConnectNumber,_j:fwTotalConnectNumberPerSecond,'fwWAFProtection':fwWAFProtection,_k:fwWAFInputRuleNumber,_l:fwWAFParameterNumber,_m:fwWAFSvrPortNumber,_n:fwWAFProfileNumber,'fwTraps':fwTraps,'fwTrapPrefix':fwTrapPrefix,_o:fwTrapHaHBFail,_p:fwTrapModeChange,_q:fwTrapPolicyStart,_r:fwTrapPolicyStop,_s:fwTrapPServerFailed,_t:fwTrapHAStatusChange,_u:fwTrapHAMemberJoin,_v:fwTrapHAMemberLeave,_w:fwTrapXMLIntrusionAttack,_x:fwTrapXMLSchemaAttack,_y:fwTrapXMLFilterAttack,_z:fwTrapXMLSigEncAttack,_A0:fwTrapXMLWSDLAttack,_A1:fwTrapXMLSqlAttack,_A2:fwTrapWAFAMethodAttack,_A3:fwTrapWAFXSSAttack,_A4:fwTrapWAFSqlAttack,_A5:fwTrapWAFExploitAttack,_A6:fwTrapWAFDisclosureAttack,_A7:fwTrapWAFAccessAttack,_A8:fwTrapWAFSPageAttack,_A9:fwTrapWAFPValidAttack,_AA:fwTrapWAFBListAttack,_AB:fwTrapWAFBLoginAttack,_AC:fwTrapWAFRobotAttack,_AD:fwTrapWAFHideFieldAttack,_AE:fwTrapWAFUrlAccessAttack,_AF:fwTrapWAFBadRobotAttack,_AG:fwTrapWAFSignatureAttack,_AH:fwTrapWAFWListAttack,'fnWafInfo':fnWafInfo,_H:fnWafInfoDetail,_P:fnWafIndex,'fnWafDate':fnWafDate,'fnWafTime':fnWafTime,'fnWafSrcIP':fnWafSrcIP,'fnWafDstIP':fnWafDstIP,'fnWafSrcPort':fnWafSrcPort,'fnWafDstPort':fnWafDstPort,'fnWafHost':fnWafHost,'fnWafURL':fnWafURL,'fwMibConformance':fwMibConformance,_AI:fwTrapGroup,_AJ:fwSystemObjectGroup,_AK:fwProxyObjectGroup,_AL:fwWAFProtectionGroup,'fwMibCompliance':fwMibCompliance})