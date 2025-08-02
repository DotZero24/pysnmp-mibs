_w='faHwSensorComplianceGroup'
_v='faNotificationObjectsComplianceGroup'
_u='faTrapsComplianceGroup'
_t='faMiscComplianceGroup'
_s='faSessionComplianceGroup'
_r='faSystemComplianceGroup'
_q='faTrapDataRateThreshold'
_p='faTrapLogRateThreshold'
_o='faTrapGenAlert'
_n='faTrapRAIDStatusChange'
_m='faTrapSystemEvent'
_l='faHwSensorEntAlarmStatus'
_k='faHwSensorEntValue'
_j='faHwSensorEntName'
_i='faHwSensorCount'
_h='faGenAlert'
_g='faIpSessExp'
_f='faIpSessToPort'
_e='faIpSessToAddr'
_d='faIpSessFromPort'
_c='faIpSessFromAddr'
_b='faIpSessProto'
_a='fa300SysSesCount'
_Z='fa300SysMemCapacity'
_Y='fa300SysDiskUsage'
_X='fa300SysDiskCapacity'
_W='fa300SysMemUsage'
_V='fa300SysCpuUsage'
_U='fa300SysVersion'
_T='fa300SysSerial'
_S='faHwSensorEntIndex'
_R='not-accessible'
_Q='faIpSessIndex'
_P='Integer32'
_O='fnGenTrapMsg'
_N='faRAIDDevIndex'
_M='faRAIDStatus'
_L='accessible-for-notify'
_K='Gauge32'
_J='sysName'
_I='SNMPv2-MIB'
_H='faSystemEvent'
_G='DisplayString'
_F='fnSysSerial'
_E='FORTINET-CORE-MIB'
_D='deprecated'
_C='read-only'
_B='current'
_A='FORTINET-FORTIANALYZER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FnIndex,fnGenTrapMsg,fnSysSerial,fnTrapsPrefix,fortinet=mibBuilder.importSymbols(_E,'FnIndex',_O,_F,'fnTrapsPrefix','fortinet')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_I,_J)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_K,_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
fnFortiAnalyzerMib=ModuleIdentity((1,3,6,1,4,1,12356,102))
if mibBuilder.loadTexts:fnFortiAnalyzerMib.setRevisions(('2009-09-21 00:00','2009-02-05 00:00'))
class FaSessProto(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,8,12,17,22,41,46,47,50,51,89,103,108,255)));namedValues=NamedValues(*(('ip',0),('icmp',1),('igmp',2),('ipip',4),('tcp',6),('egp',8),('pup',12),('udp',17),('idp',22),('ipv6',41),('rsvp',46),('gre',47),('esp',50),('ah',51),('ospf',89),('pim',103),('comp',108),('raw',255)))
class FaRAIDStatusCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('arrayOK',1),('arrayDegraded',2),('arrayInoperable',3),('arrayRebuilding',4),('arrayRebuildingStarted',5),('arrayRebuildingFinished',6),('arrayInitializing',7),('arrayInitializingStarted',8),('arrayInitializingFinished',9),('diskOK',10),('diskDegraded',11),('diskFailEvent',12)))
class FaSysEventCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('systemHalt',1),('systemReboot',2),('upgradeConfig',3),('systemUpgrade',4),('logdiskFormat',5)))
_FaTraps_ObjectIdentity=ObjectIdentity
faTraps=_FaTraps_ObjectIdentity((1,3,6,1,4,1,12356,102,0))
_FaTrapPrefix_ObjectIdentity=ObjectIdentity
faTrapPrefix=_FaTrapPrefix_ObjectIdentity((1,3,6,1,4,1,12356,102,0,0))
_FaTrapObject_ObjectIdentity=ObjectIdentity
faTrapObject=_FaTrapObject_ObjectIdentity((1,3,6,1,4,1,12356,102,0,1))
_FaSystemEvent_Type=FaSysEventCode
_FaSystemEvent_Object=MibScalar
faSystemEvent=_FaSystemEvent_Object((1,3,6,1,4,1,12356,102,0,1,1),_FaSystemEvent_Type())
faSystemEvent.setMaxAccess(_L)
if mibBuilder.loadTexts:faSystemEvent.setStatus(_B)
_FaRAIDStatus_Type=FaRAIDStatusCode
_FaRAIDStatus_Object=MibScalar
faRAIDStatus=_FaRAIDStatus_Object((1,3,6,1,4,1,12356,102,0,1,2),_FaRAIDStatus_Type())
faRAIDStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:faRAIDStatus.setStatus(_B)
class _FaRAIDDevIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FaRAIDDevIndex_Type.__name__=_G
_FaRAIDDevIndex_Object=MibScalar
faRAIDDevIndex=_FaRAIDDevIndex_Object((1,3,6,1,4,1,12356,102,0,1,3),_FaRAIDDevIndex_Type())
faRAIDDevIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:faRAIDDevIndex.setStatus(_B)
_FaGenAlert_Type=DisplayString
_FaGenAlert_Object=MibScalar
faGenAlert=_FaGenAlert_Object((1,3,6,1,4,1,12356,102,0,1,4),_FaGenAlert_Type())
faGenAlert.setMaxAccess(_C)
if mibBuilder.loadTexts:faGenAlert.setStatus(_B)
_FaModel_ObjectIdentity=ObjectIdentity
faModel=_FaModel_ObjectIdentity((1,3,6,1,4,1,12356,102,1))
_Faz100_ObjectIdentity=ObjectIdentity
faz100=_Faz100_ObjectIdentity((1,3,6,1,4,1,12356,102,1,1000))
_Faz100A_ObjectIdentity=ObjectIdentity
faz100A=_Faz100A_ObjectIdentity((1,3,6,1,4,1,12356,102,1,1001))
_Faz100B_ObjectIdentity=ObjectIdentity
faz100B=_Faz100B_ObjectIdentity((1,3,6,1,4,1,12356,102,1,1002))
_Faz100C_ObjectIdentity=ObjectIdentity
faz100C=_Faz100C_ObjectIdentity((1,3,6,1,4,1,12356,102,1,1003))
_Faz400_ObjectIdentity=ObjectIdentity
faz400=_Faz400_ObjectIdentity((1,3,6,1,4,1,12356,102,1,4000))
_Faz400B_ObjectIdentity=ObjectIdentity
faz400B=_Faz400B_ObjectIdentity((1,3,6,1,4,1,12356,102,1,4002))
_Faz800_ObjectIdentity=ObjectIdentity
faz800=_Faz800_ObjectIdentity((1,3,6,1,4,1,12356,102,1,8000))
_Faz800B_ObjectIdentity=ObjectIdentity
faz800B=_Faz800B_ObjectIdentity((1,3,6,1,4,1,12356,102,1,8002))
_Faz1000B_ObjectIdentity=ObjectIdentity
faz1000B=_Faz1000B_ObjectIdentity((1,3,6,1,4,1,12356,102,1,10002))
_Faz2000_ObjectIdentity=ObjectIdentity
faz2000=_Faz2000_ObjectIdentity((1,3,6,1,4,1,12356,102,1,20000))
_Faz2000A_ObjectIdentity=ObjectIdentity
faz2000A=_Faz2000A_ObjectIdentity((1,3,6,1,4,1,12356,102,1,20001))
_Faz4000_ObjectIdentity=ObjectIdentity
faz4000=_Faz4000_ObjectIdentity((1,3,6,1,4,1,12356,102,1,40000))
_Faz4000A_ObjectIdentity=ObjectIdentity
faz4000A=_Faz4000A_ObjectIdentity((1,3,6,1,4,1,12356,102,1,40001))
_FaInetProto_ObjectIdentity=ObjectIdentity
faInetProto=_FaInetProto_ObjectIdentity((1,3,6,1,4,1,12356,102,2))
_FaInetProtoInfo_ObjectIdentity=ObjectIdentity
faInetProtoInfo=_FaInetProtoInfo_ObjectIdentity((1,3,6,1,4,1,12356,102,2,1))
_FaInetProtoTables_ObjectIdentity=ObjectIdentity
faInetProtoTables=_FaInetProtoTables_ObjectIdentity((1,3,6,1,4,1,12356,102,2,2))
_FaIpSessTable_Object=MibTable
faIpSessTable=_FaIpSessTable_Object((1,3,6,1,4,1,12356,102,2,2,1))
if mibBuilder.loadTexts:faIpSessTable.setStatus(_B)
_FaIpSessEntry_Object=MibTableRow
faIpSessEntry=_FaIpSessEntry_Object((1,3,6,1,4,1,12356,102,2,2,1,1))
faIpSessEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:faIpSessEntry.setStatus(_B)
_FaIpSessIndex_Type=FnIndex
_FaIpSessIndex_Object=MibTableColumn
faIpSessIndex=_FaIpSessIndex_Object((1,3,6,1,4,1,12356,102,2,2,1,1,1),_FaIpSessIndex_Type())
faIpSessIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:faIpSessIndex.setStatus(_B)
_FaIpSessProto_Type=FaSessProto
_FaIpSessProto_Object=MibTableColumn
faIpSessProto=_FaIpSessProto_Object((1,3,6,1,4,1,12356,102,2,2,1,1,2),_FaIpSessProto_Type())
faIpSessProto.setMaxAccess(_C)
if mibBuilder.loadTexts:faIpSessProto.setStatus(_B)
_FaIpSessFromAddr_Type=IpAddress
_FaIpSessFromAddr_Object=MibTableColumn
faIpSessFromAddr=_FaIpSessFromAddr_Object((1,3,6,1,4,1,12356,102,2,2,1,1,3),_FaIpSessFromAddr_Type())
faIpSessFromAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:faIpSessFromAddr.setStatus(_B)
_FaIpSessFromPort_Type=InetPortNumber
_FaIpSessFromPort_Object=MibTableColumn
faIpSessFromPort=_FaIpSessFromPort_Object((1,3,6,1,4,1,12356,102,2,2,1,1,4),_FaIpSessFromPort_Type())
faIpSessFromPort.setMaxAccess(_C)
if mibBuilder.loadTexts:faIpSessFromPort.setStatus(_B)
_FaIpSessToAddr_Type=IpAddress
_FaIpSessToAddr_Object=MibTableColumn
faIpSessToAddr=_FaIpSessToAddr_Object((1,3,6,1,4,1,12356,102,2,2,1,1,5),_FaIpSessToAddr_Type())
faIpSessToAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:faIpSessToAddr.setStatus(_B)
_FaIpSessToPort_Type=InetPortNumber
_FaIpSessToPort_Object=MibTableColumn
faIpSessToPort=_FaIpSessToPort_Object((1,3,6,1,4,1,12356,102,2,2,1,1,6),_FaIpSessToPort_Type())
faIpSessToPort.setMaxAccess(_C)
if mibBuilder.loadTexts:faIpSessToPort.setStatus(_B)
_FaIpSessExp_Type=Counter32
_FaIpSessExp_Object=MibTableColumn
faIpSessExp=_FaIpSessExp_Object((1,3,6,1,4,1,12356,102,2,2,1,1,7),_FaIpSessExp_Type())
faIpSessExp.setMaxAccess(_C)
if mibBuilder.loadTexts:faIpSessExp.setStatus(_B)
_Fa300Compat_ObjectIdentity=ObjectIdentity
fa300Compat=_Fa300Compat_ObjectIdentity((1,3,6,1,4,1,12356,102,99))
_FaHwSensors_ObjectIdentity=ObjectIdentity
faHwSensors=_FaHwSensors_ObjectIdentity((1,3,6,1,4,1,12356,102,99,1))
_FaHwSensorCount_Type=Integer32
_FaHwSensorCount_Object=MibScalar
faHwSensorCount=_FaHwSensorCount_Object((1,3,6,1,4,1,12356,102,99,1,1),_FaHwSensorCount_Type())
faHwSensorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:faHwSensorCount.setStatus(_D)
_FaHwSensorTable_Object=MibTable
faHwSensorTable=_FaHwSensorTable_Object((1,3,6,1,4,1,12356,102,99,1,2))
if mibBuilder.loadTexts:faHwSensorTable.setStatus(_D)
_FaHwSensorEntry_Object=MibTableRow
faHwSensorEntry=_FaHwSensorEntry_Object((1,3,6,1,4,1,12356,102,99,1,2,1))
faHwSensorEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:faHwSensorEntry.setStatus(_D)
_FaHwSensorEntIndex_Type=FnIndex
_FaHwSensorEntIndex_Object=MibTableColumn
faHwSensorEntIndex=_FaHwSensorEntIndex_Object((1,3,6,1,4,1,12356,102,99,1,2,1,1),_FaHwSensorEntIndex_Type())
faHwSensorEntIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:faHwSensorEntIndex.setStatus(_D)
_FaHwSensorEntName_Type=DisplayString
_FaHwSensorEntName_Object=MibTableColumn
faHwSensorEntName=_FaHwSensorEntName_Object((1,3,6,1,4,1,12356,102,99,1,2,1,2),_FaHwSensorEntName_Type())
faHwSensorEntName.setMaxAccess(_C)
if mibBuilder.loadTexts:faHwSensorEntName.setStatus(_D)
_FaHwSensorEntValue_Type=DisplayString
_FaHwSensorEntValue_Object=MibTableColumn
faHwSensorEntValue=_FaHwSensorEntValue_Object((1,3,6,1,4,1,12356,102,99,1,2,1,3),_FaHwSensorEntValue_Type())
faHwSensorEntValue.setMaxAccess(_C)
if mibBuilder.loadTexts:faHwSensorEntValue.setStatus(_D)
class _FaHwSensorEntAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_FaHwSensorEntAlarmStatus_Type.__name__=_P
_FaHwSensorEntAlarmStatus_Object=MibTableColumn
faHwSensorEntAlarmStatus=_FaHwSensorEntAlarmStatus_Object((1,3,6,1,4,1,12356,102,99,1,2,1,4),_FaHwSensorEntAlarmStatus_Type())
faHwSensorEntAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:faHwSensorEntAlarmStatus.setStatus(_D)
_Fa300System_ObjectIdentity=ObjectIdentity
fa300System=_Fa300System_ObjectIdentity((1,3,6,1,4,1,12356,102,99,2))
class _Fa300SysSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Fa300SysSerial_Type.__name__=_G
_Fa300SysSerial_Object=MibScalar
fa300SysSerial=_Fa300SysSerial_Object((1,3,6,1,4,1,12356,102,99,2,1),_Fa300SysSerial_Type())
fa300SysSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:fa300SysSerial.setStatus(_B)
class _Fa300SysVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Fa300SysVersion_Type.__name__=_G
_Fa300SysVersion_Object=MibScalar
fa300SysVersion=_Fa300SysVersion_Object((1,3,6,1,4,1,12356,102,99,2,2),_Fa300SysVersion_Type())
fa300SysVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fa300SysVersion.setStatus(_B)
class _Fa300SysCpuUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fa300SysCpuUsage_Type.__name__=_K
_Fa300SysCpuUsage_Object=MibScalar
fa300SysCpuUsage=_Fa300SysCpuUsage_Object((1,3,6,1,4,1,12356,102,99,2,3),_Fa300SysCpuUsage_Type())
fa300SysCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fa300SysCpuUsage.setStatus(_B)
class _Fa300SysMemUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fa300SysMemUsage_Type.__name__=_K
_Fa300SysMemUsage_Object=MibScalar
fa300SysMemUsage=_Fa300SysMemUsage_Object((1,3,6,1,4,1,12356,102,99,2,4),_Fa300SysMemUsage_Type())
fa300SysMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fa300SysMemUsage.setStatus(_B)
_Fa300SysSesCount_Type=Gauge32
_Fa300SysSesCount_Object=MibScalar
fa300SysSesCount=_Fa300SysSesCount_Object((1,3,6,1,4,1,12356,102,99,2,5),_Fa300SysSesCount_Type())
fa300SysSesCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fa300SysSesCount.setStatus(_B)
_Fa300SysDiskCapacity_Type=Gauge32
_Fa300SysDiskCapacity_Object=MibScalar
fa300SysDiskCapacity=_Fa300SysDiskCapacity_Object((1,3,6,1,4,1,12356,102,99,2,6),_Fa300SysDiskCapacity_Type())
fa300SysDiskCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:fa300SysDiskCapacity.setStatus(_B)
_Fa300SysDiskUsage_Type=Gauge32
_Fa300SysDiskUsage_Object=MibScalar
fa300SysDiskUsage=_Fa300SysDiskUsage_Object((1,3,6,1,4,1,12356,102,99,2,7),_Fa300SysDiskUsage_Type())
fa300SysDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fa300SysDiskUsage.setStatus(_B)
_Fa300SysMemCapacity_Type=Gauge32
_Fa300SysMemCapacity_Object=MibScalar
fa300SysMemCapacity=_Fa300SysMemCapacity_Object((1,3,6,1,4,1,12356,102,99,2,8),_Fa300SysMemCapacity_Type())
fa300SysMemCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:fa300SysMemCapacity.setStatus(_B)
_FaMIBConformance_ObjectIdentity=ObjectIdentity
faMIBConformance=_FaMIBConformance_ObjectIdentity((1,3,6,1,4,1,12356,102,100))
faSystemComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,102,100,1))
faSystemComplianceGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_H)))
if mibBuilder.loadTexts:faSystemComplianceGroup.setStatus(_B)
faSessionComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,102,100,3))
faSessionComplianceGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:faSessionComplianceGroup.setStatus(_B)
faMiscComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,102,100,4))
faMiscComplianceGroup.setObjects((_A,_h))
if mibBuilder.loadTexts:faMiscComplianceGroup.setStatus(_B)
faHwSensorComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,102,100,5))
faHwSensorComplianceGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:faHwSensorComplianceGroup.setStatus(_D)
faNotificationObjectsComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,102,100,6))
faNotificationObjectsComplianceGroup.setObjects(*((_A,_H),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:faNotificationObjectsComplianceGroup.setStatus(_B)
faTrapLogRateThreshold=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,1005))
faTrapLogRateThreshold.setObjects(*((_E,_F),(_I,_J)))
if mibBuilder.loadTexts:faTrapLogRateThreshold.setStatus(_B)
faTrapDataRateThreshold=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,1006))
faTrapDataRateThreshold.setObjects(*((_E,_F),(_I,_J)))
if mibBuilder.loadTexts:faTrapDataRateThreshold.setStatus(_B)
faTrapSystemEvent=NotificationType((1,3,6,1,4,1,12356,102,0,0,1001))
faTrapSystemEvent.setObjects(*((_E,_F),(_A,_H)))
if mibBuilder.loadTexts:faTrapSystemEvent.setStatus(_B)
faTrapRAIDStatusChange=NotificationType((1,3,6,1,4,1,12356,102,0,0,1002))
faTrapRAIDStatusChange.setObjects(*((_E,_F),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:faTrapRAIDStatusChange.setStatus(_B)
faTrapGenAlert=NotificationType((1,3,6,1,4,1,12356,102,0,0,1003))
faTrapGenAlert.setObjects(*((_E,_F),(_E,_O)))
if mibBuilder.loadTexts:faTrapGenAlert.setStatus(_B)
faTrapsComplianceGroup=NotificationGroup((1,3,6,1,4,1,12356,102,100,2))
faTrapsComplianceGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:faTrapsComplianceGroup.setStatus(_B)
faMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,102,100,100))
faMIBCompliance.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:faMIBCompliance.setStatus(_B)
faObsoleteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,102,100,101))
faObsoleteMIBCompliance.setObjects((_A,_w))
if mibBuilder.loadTexts:faObsoleteMIBCompliance.setStatus(_D)
mibBuilder.exportSymbols(_A,**{'FaSessProto':FaSessProto,'FaRAIDStatusCode':FaRAIDStatusCode,'FaSysEventCode':FaSysEventCode,_p:faTrapLogRateThreshold,_q:faTrapDataRateThreshold,'fnFortiAnalyzerMib':fnFortiAnalyzerMib,'faTraps':faTraps,'faTrapPrefix':faTrapPrefix,_m:faTrapSystemEvent,_n:faTrapRAIDStatusChange,_o:faTrapGenAlert,'faTrapObject':faTrapObject,_H:faSystemEvent,_M:faRAIDStatus,_N:faRAIDDevIndex,_h:faGenAlert,'faModel':faModel,'faz100':faz100,'faz100A':faz100A,'faz100B':faz100B,'faz100C':faz100C,'faz400':faz400,'faz400B':faz400B,'faz800':faz800,'faz800B':faz800B,'faz1000B':faz1000B,'faz2000':faz2000,'faz2000A':faz2000A,'faz4000':faz4000,'faz4000A':faz4000A,'faInetProto':faInetProto,'faInetProtoInfo':faInetProtoInfo,'faInetProtoTables':faInetProtoTables,'faIpSessTable':faIpSessTable,'faIpSessEntry':faIpSessEntry,_Q:faIpSessIndex,_b:faIpSessProto,_c:faIpSessFromAddr,_d:faIpSessFromPort,_e:faIpSessToAddr,_f:faIpSessToPort,_g:faIpSessExp,'fa300Compat':fa300Compat,'faHwSensors':faHwSensors,_i:faHwSensorCount,'faHwSensorTable':faHwSensorTable,'faHwSensorEntry':faHwSensorEntry,_S:faHwSensorEntIndex,_j:faHwSensorEntName,_k:faHwSensorEntValue,_l:faHwSensorEntAlarmStatus,'fa300System':fa300System,_T:fa300SysSerial,_U:fa300SysVersion,_V:fa300SysCpuUsage,_W:fa300SysMemUsage,_a:fa300SysSesCount,_X:fa300SysDiskCapacity,_Y:fa300SysDiskUsage,_Z:fa300SysMemCapacity,'faMIBConformance':faMIBConformance,_r:faSystemComplianceGroup,_u:faTrapsComplianceGroup,_s:faSessionComplianceGroup,_t:faMiscComplianceGroup,_w:faHwSensorComplianceGroup,_v:faNotificationObjectsComplianceGroup,'faMIBCompliance':faMIBCompliance,'faObsoleteMIBCompliance':faObsoleteMIBCompliance})