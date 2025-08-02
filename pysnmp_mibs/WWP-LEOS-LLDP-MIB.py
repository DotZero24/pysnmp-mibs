_AO='wwpLeosLldpOptLocSysGroup'
_AN='wwpLeosLldpRemSysGroup'
_AM='wwpLeosLldpLocSysGroup'
_AL='wwpLeosLldpStatsGroup'
_AK='wwpLeosLldpConfigGroup'
_AJ='wwpLeosLldpPortConfigReqPortSpeed'
_AI='wwpLeosLldpPortConfigOperPortSpeed'
_AH='wwpLeosLldpRemOrgDefInfo'
_AG='wwpLeosLldpRemUnknownTLVInfo'
_AF='wwpLeosLldpRemManAddrOID'
_AE='wwpLeosLldpRemManAddrIfId'
_AD='wwpLeosLldpRemManAddrIfSubtype'
_AC='wwpLeosLldpRemSysCapEnabled'
_AB='wwpLeosLldpRemSysCapSupported'
_AA='wwpLeosLldpRemSysDesc'
_A9='wwpLeosLldpRemSysName'
_A8='wwpLeosLldpRemPortDesc'
_A7='wwpLeosLldpRemRemotePort'
_A6='wwpLeosLldpRemRemotePortType'
_A5='wwpLeosLldpRemRemoteChassis'
_A4='wwpLeosLldpRemRemoteChassisType'
_A3='wwpLeosLldpLocManAddrOID'
_A2='wwpLeosLldpLocManAddrIfId'
_A1='wwpLeosLldpLocManAddrIfSubtype'
_A0='wwpLeosLldpLocSysCapEnabled'
_z='wwpLeosLldpLocSysCapSupported'
_y='wwpLeosLldpLocSysName'
_x='wwpLeosLldpLocSysDesc'
_w='wwpLeosLldpLocPortDesc'
_v='wwpLeosLldpLocPortId'
_u='wwpLeosLldpLocPortType'
_t='wwpLeosLldpLocChassisId'
_s='wwpLeosLldpLocChassisType'
_r='wwpLeosLldpCounterDiscontinuityTime'
_q='wwpLeosLldpStatsTLVsUnrecognizedTotal'
_p='wwpLeosLldpStatsTLVsDiscardedTotal'
_o='wwpLeosLldpStatsTLVsInErrors'
_n='wwpLeosLldpStatsFramesOutTotal'
_m='wwpLeosLldpStatsFramesInTotal'
_l='wwpLeosLldpStatsFramesInErrors'
_k='wwpLeosLldpStatsFramesDiscardedTotal'
_j='wwpLeosLldpManAddrPortsTxEnable'
_i='wwpLeosLldpPortConfigTLVsTxEnable'
_h='wwpLeosLldpPortConfigAdminStatus'
_g='wwpLeosLldpTxDelay'
_f='wwpLeosLldpReinitDelay'
_e='wwpLeosLldpMessageTxHoldMultiplier'
_d='wwpLeosLldpMessageTxInterval'
_c='wwpLeosLldpConfigManAddrEntry'
_b='wwpLeosLldpRemOrgDefInfoIndex'
_a='wwpLeosLldpRemOrgDefInfoSubtype'
_Z='wwpLeosLldpRemOrgDefInfoOUI'
_Y='wwpLeosLldpRemManAddr'
_X='wwpLeosLldpRemManAddrType'
_W='wwpLeosLldpLocManAddr'
_V='wwpLeosLldpLocManAddrType'
_U='wwpLeosLldpLocPortNum'
_T='wwpLeosLldpStatsPortNum'
_S='networkAddress'
_R='macAddress'
_Q='backplaneEntPhysicalAlias'
_P='portEntPhysicalAlias'
_O='ifAlias'
_N='wwpLeosLldpPortConfigPortNum'
_M='seconds'
_L='OctetString'
_K='wwpLeosLldpRemIndex'
_J='wwpLeosLldpRemLocalPortNum'
_I='wwpLeosLldpRemTimeMark'
_H='current'
_G='SnmpAdminString'
_F='read-write'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='WWP-LEOS-LLDP-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosLldpMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,26))
if mibBuilder.loadTexts:wwpLeosLldpMIB.setRevisions(('2004-04-18 00:00','2003-04-23 00:00'))
class TimeFilter(TextualConvention,TimeTicks):status=_A
class SnmpAdminString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class WwpLeosLldpChassisIdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('entPhysicalAlias',1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),('local',7)))
class WwpLeosLldpChassisId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class WwpLeosLldpPortIdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),('local',6)))
class WwpLeosLldpPortId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class WwpLeosLldpManAddrIfSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('ifIndex',2),('systemPortNumber',3)))
class WwpLeosLldpManAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class WwpLeosLldpSystemCapabilitiesMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('repeater',0),('bridge',1),('accessPoint',2),('router',3),('telephone',4),('wirelessStation',5),('stationOnly',6)))
class WwpLeosLldpPortNumber(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
class WwpLeosLldpPortList(TextualConvention,OctetString):status=_A
_WwpLeosLldpMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosLldpMIBObjects=_WwpLeosLldpMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,1))
_WwpLeosLldpConfiguration_ObjectIdentity=ObjectIdentity
wwpLeosLldpConfiguration=_WwpLeosLldpConfiguration_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,1,1))
class _WwpLeosLldpMessageTxInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,32768))
_WwpLeosLldpMessageTxInterval_Type.__name__=_E
_WwpLeosLldpMessageTxInterval_Object=MibScalar
wwpLeosLldpMessageTxInterval=_WwpLeosLldpMessageTxInterval_Object((1,3,6,1,4,1,6141,2,60,26,1,1,1),_WwpLeosLldpMessageTxInterval_Type())
wwpLeosLldpMessageTxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpMessageTxInterval.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosLldpMessageTxInterval.setUnits(_M)
class _WwpLeosLldpMessageTxHoldMultiplier_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_WwpLeosLldpMessageTxHoldMultiplier_Type.__name__=_E
_WwpLeosLldpMessageTxHoldMultiplier_Object=MibScalar
wwpLeosLldpMessageTxHoldMultiplier=_WwpLeosLldpMessageTxHoldMultiplier_Object((1,3,6,1,4,1,6141,2,60,26,1,1,2),_WwpLeosLldpMessageTxHoldMultiplier_Type())
wwpLeosLldpMessageTxHoldMultiplier.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpMessageTxHoldMultiplier.setStatus(_A)
class _WwpLeosLldpReinitDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosLldpReinitDelay_Type.__name__=_E
_WwpLeosLldpReinitDelay_Object=MibScalar
wwpLeosLldpReinitDelay=_WwpLeosLldpReinitDelay_Object((1,3,6,1,4,1,6141,2,60,26,1,1,3),_WwpLeosLldpReinitDelay_Type())
wwpLeosLldpReinitDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpReinitDelay.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosLldpReinitDelay.setUnits(_M)
class _WwpLeosLldpTxDelay_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_WwpLeosLldpTxDelay_Type.__name__=_E
_WwpLeosLldpTxDelay_Object=MibScalar
wwpLeosLldpTxDelay=_WwpLeosLldpTxDelay_Object((1,3,6,1,4,1,6141,2,60,26,1,1,4),_WwpLeosLldpTxDelay_Type())
wwpLeosLldpTxDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpTxDelay.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosLldpTxDelay.setUnits(_M)
_WwpLeosLldpPortConfigTable_Object=MibTable
wwpLeosLldpPortConfigTable=_WwpLeosLldpPortConfigTable_Object((1,3,6,1,4,1,6141,2,60,26,1,1,5))
if mibBuilder.loadTexts:wwpLeosLldpPortConfigTable.setStatus(_A)
_WwpLeosLldpPortConfigEntry_Object=MibTableRow
wwpLeosLldpPortConfigEntry=_WwpLeosLldpPortConfigEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,1,5,1))
wwpLeosLldpPortConfigEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:wwpLeosLldpPortConfigEntry.setStatus(_A)
_WwpLeosLldpPortConfigPortNum_Type=WwpLeosLldpPortNumber
_WwpLeosLldpPortConfigPortNum_Object=MibTableColumn
wwpLeosLldpPortConfigPortNum=_WwpLeosLldpPortConfigPortNum_Object((1,3,6,1,4,1,6141,2,60,26,1,1,5,1,1),_WwpLeosLldpPortConfigPortNum_Type())
wwpLeosLldpPortConfigPortNum.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:wwpLeosLldpPortConfigPortNum.setStatus(_A)
class _WwpLeosLldpPortConfigAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('txOnly',1),('rxOnly',2),('txAndRx',3),('disabled',4)))
_WwpLeosLldpPortConfigAdminStatus_Type.__name__=_E
_WwpLeosLldpPortConfigAdminStatus_Object=MibTableColumn
wwpLeosLldpPortConfigAdminStatus=_WwpLeosLldpPortConfigAdminStatus_Object((1,3,6,1,4,1,6141,2,60,26,1,1,5,1,2),_WwpLeosLldpPortConfigAdminStatus_Type())
wwpLeosLldpPortConfigAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpPortConfigAdminStatus.setStatus(_A)
class _WwpLeosLldpPortConfigTLVsTxEnable_Type(Bits):defaultBinValue='00001111';namedValues=NamedValues(*(('portDesc',4),('sysName',5),('sysDesc',6),('sysCap',7)))
_WwpLeosLldpPortConfigTLVsTxEnable_Type.__name__='Bits'
_WwpLeosLldpPortConfigTLVsTxEnable_Object=MibTableColumn
wwpLeosLldpPortConfigTLVsTxEnable=_WwpLeosLldpPortConfigTLVsTxEnable_Object((1,3,6,1,4,1,6141,2,60,26,1,1,5,1,3),_WwpLeosLldpPortConfigTLVsTxEnable_Type())
wwpLeosLldpPortConfigTLVsTxEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpPortConfigTLVsTxEnable.setStatus(_A)
_WwpLeosLldpPortConfigStatsClear_Type=TruthValue
_WwpLeosLldpPortConfigStatsClear_Object=MibTableColumn
wwpLeosLldpPortConfigStatsClear=_WwpLeosLldpPortConfigStatsClear_Object((1,3,6,1,4,1,6141,2,60,26,1,1,5,1,4),_WwpLeosLldpPortConfigStatsClear_Type())
wwpLeosLldpPortConfigStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpPortConfigStatsClear.setStatus(_H)
_WwpLeosLldpPortConfigOperPortSpeed_Type=Unsigned32
_WwpLeosLldpPortConfigOperPortSpeed_Object=MibTableColumn
wwpLeosLldpPortConfigOperPortSpeed=_WwpLeosLldpPortConfigOperPortSpeed_Object((1,3,6,1,4,1,6141,2,60,26,1,1,5,1,5),_WwpLeosLldpPortConfigOperPortSpeed_Type())
wwpLeosLldpPortConfigOperPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpPortConfigOperPortSpeed.setStatus(_H)
_WwpLeosLldpPortConfigReqPortSpeed_Type=Unsigned32
_WwpLeosLldpPortConfigReqPortSpeed_Object=MibTableColumn
wwpLeosLldpPortConfigReqPortSpeed=_WwpLeosLldpPortConfigReqPortSpeed_Object((1,3,6,1,4,1,6141,2,60,26,1,1,5,1,6),_WwpLeosLldpPortConfigReqPortSpeed_Type())
wwpLeosLldpPortConfigReqPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpPortConfigReqPortSpeed.setStatus(_H)
_WwpLeosLldpConfigManAddrTable_Object=MibTable
wwpLeosLldpConfigManAddrTable=_WwpLeosLldpConfigManAddrTable_Object((1,3,6,1,4,1,6141,2,60,26,1,1,6))
if mibBuilder.loadTexts:wwpLeosLldpConfigManAddrTable.setStatus(_A)
_WwpLeosLldpConfigManAddrEntry_Object=MibTableRow
wwpLeosLldpConfigManAddrEntry=_WwpLeosLldpConfigManAddrEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,1,6,1))
if mibBuilder.loadTexts:wwpLeosLldpConfigManAddrEntry.setStatus(_A)
_WwpLeosLldpManAddrPortsTxEnable_Type=WwpLeosLldpPortList
_WwpLeosLldpManAddrPortsTxEnable_Object=MibTableColumn
wwpLeosLldpManAddrPortsTxEnable=_WwpLeosLldpManAddrPortsTxEnable_Object((1,3,6,1,4,1,6141,2,60,26,1,1,6,1,1),_WwpLeosLldpManAddrPortsTxEnable_Type())
wwpLeosLldpManAddrPortsTxEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpManAddrPortsTxEnable.setStatus(_A)
_WwpLeosLldpStatistics_ObjectIdentity=ObjectIdentity
wwpLeosLldpStatistics=_WwpLeosLldpStatistics_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,1,2))
_WwpLeosLldpStatsTable_Object=MibTable
wwpLeosLldpStatsTable=_WwpLeosLldpStatsTable_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1))
if mibBuilder.loadTexts:wwpLeosLldpStatsTable.setStatus(_A)
_WwpLeosLldpStatsEntry_Object=MibTableRow
wwpLeosLldpStatsEntry=_WwpLeosLldpStatsEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1))
wwpLeosLldpStatsEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:wwpLeosLldpStatsEntry.setStatus(_A)
_WwpLeosLldpStatsPortNum_Type=WwpLeosLldpPortNumber
_WwpLeosLldpStatsPortNum_Object=MibTableColumn
wwpLeosLldpStatsPortNum=_WwpLeosLldpStatsPortNum_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,1),_WwpLeosLldpStatsPortNum_Type())
wwpLeosLldpStatsPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpStatsPortNum.setStatus(_A)
_WwpLeosLldpStatsFramesDiscardedTotal_Type=Counter32
_WwpLeosLldpStatsFramesDiscardedTotal_Object=MibTableColumn
wwpLeosLldpStatsFramesDiscardedTotal=_WwpLeosLldpStatsFramesDiscardedTotal_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,2),_WwpLeosLldpStatsFramesDiscardedTotal_Type())
wwpLeosLldpStatsFramesDiscardedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpStatsFramesDiscardedTotal.setStatus(_A)
_WwpLeosLldpStatsFramesInErrors_Type=Counter32
_WwpLeosLldpStatsFramesInErrors_Object=MibTableColumn
wwpLeosLldpStatsFramesInErrors=_WwpLeosLldpStatsFramesInErrors_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,3),_WwpLeosLldpStatsFramesInErrors_Type())
wwpLeosLldpStatsFramesInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpStatsFramesInErrors.setStatus(_A)
_WwpLeosLldpStatsFramesInTotal_Type=Counter32
_WwpLeosLldpStatsFramesInTotal_Object=MibTableColumn
wwpLeosLldpStatsFramesInTotal=_WwpLeosLldpStatsFramesInTotal_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,4),_WwpLeosLldpStatsFramesInTotal_Type())
wwpLeosLldpStatsFramesInTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpStatsFramesInTotal.setStatus(_A)
_WwpLeosLldpStatsFramesOutTotal_Type=Counter32
_WwpLeosLldpStatsFramesOutTotal_Object=MibTableColumn
wwpLeosLldpStatsFramesOutTotal=_WwpLeosLldpStatsFramesOutTotal_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,5),_WwpLeosLldpStatsFramesOutTotal_Type())
wwpLeosLldpStatsFramesOutTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpStatsFramesOutTotal.setStatus(_A)
_WwpLeosLldpStatsTLVsInErrors_Type=Counter32
_WwpLeosLldpStatsTLVsInErrors_Object=MibTableColumn
wwpLeosLldpStatsTLVsInErrors=_WwpLeosLldpStatsTLVsInErrors_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,6),_WwpLeosLldpStatsTLVsInErrors_Type())
wwpLeosLldpStatsTLVsInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpStatsTLVsInErrors.setStatus(_A)
_WwpLeosLldpStatsTLVsDiscardedTotal_Type=Counter32
_WwpLeosLldpStatsTLVsDiscardedTotal_Object=MibTableColumn
wwpLeosLldpStatsTLVsDiscardedTotal=_WwpLeosLldpStatsTLVsDiscardedTotal_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,7),_WwpLeosLldpStatsTLVsDiscardedTotal_Type())
wwpLeosLldpStatsTLVsDiscardedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpStatsTLVsDiscardedTotal.setStatus(_A)
_WwpLeosLldpStatsTLVsUnrecognizedTotal_Type=Counter32
_WwpLeosLldpStatsTLVsUnrecognizedTotal_Object=MibTableColumn
wwpLeosLldpStatsTLVsUnrecognizedTotal=_WwpLeosLldpStatsTLVsUnrecognizedTotal_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,8),_WwpLeosLldpStatsTLVsUnrecognizedTotal_Type())
wwpLeosLldpStatsTLVsUnrecognizedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpStatsTLVsUnrecognizedTotal.setStatus(_A)
_WwpLeosLldpCounterDiscontinuityTime_Type=TimeStamp
_WwpLeosLldpCounterDiscontinuityTime_Object=MibTableColumn
wwpLeosLldpCounterDiscontinuityTime=_WwpLeosLldpCounterDiscontinuityTime_Object((1,3,6,1,4,1,6141,2,60,26,1,2,1,1,9),_WwpLeosLldpCounterDiscontinuityTime_Type())
wwpLeosLldpCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpCounterDiscontinuityTime.setStatus(_A)
_WwpLeosLldpLocalSystemData_ObjectIdentity=ObjectIdentity
wwpLeosLldpLocalSystemData=_WwpLeosLldpLocalSystemData_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,1,3))
_WwpLeosLldpLocChassisType_Type=WwpLeosLldpChassisIdType
_WwpLeosLldpLocChassisType_Object=MibScalar
wwpLeosLldpLocChassisType=_WwpLeosLldpLocChassisType_Object((1,3,6,1,4,1,6141,2,60,26,1,3,1),_WwpLeosLldpLocChassisType_Type())
wwpLeosLldpLocChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocChassisType.setStatus(_A)
_WwpLeosLldpLocChassisId_Type=WwpLeosLldpChassisId
_WwpLeosLldpLocChassisId_Object=MibScalar
wwpLeosLldpLocChassisId=_WwpLeosLldpLocChassisId_Object((1,3,6,1,4,1,6141,2,60,26,1,3,2),_WwpLeosLldpLocChassisId_Type())
wwpLeosLldpLocChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocChassisId.setStatus(_A)
class _WwpLeosLldpLocSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpLeosLldpLocSysName_Type.__name__=_G
_WwpLeosLldpLocSysName_Object=MibScalar
wwpLeosLldpLocSysName=_WwpLeosLldpLocSysName_Object((1,3,6,1,4,1,6141,2,60,26,1,3,3),_WwpLeosLldpLocSysName_Type())
wwpLeosLldpLocSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocSysName.setStatus(_A)
class _WwpLeosLldpLocSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpLeosLldpLocSysDesc_Type.__name__=_G
_WwpLeosLldpLocSysDesc_Object=MibScalar
wwpLeosLldpLocSysDesc=_WwpLeosLldpLocSysDesc_Object((1,3,6,1,4,1,6141,2,60,26,1,3,4),_WwpLeosLldpLocSysDesc_Type())
wwpLeosLldpLocSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocSysDesc.setStatus(_A)
_WwpLeosLldpLocSysCapSupported_Type=WwpLeosLldpSystemCapabilitiesMap
_WwpLeosLldpLocSysCapSupported_Object=MibScalar
wwpLeosLldpLocSysCapSupported=_WwpLeosLldpLocSysCapSupported_Object((1,3,6,1,4,1,6141,2,60,26,1,3,5),_WwpLeosLldpLocSysCapSupported_Type())
wwpLeosLldpLocSysCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocSysCapSupported.setStatus(_A)
_WwpLeosLldpLocSysCapEnabled_Type=WwpLeosLldpSystemCapabilitiesMap
_WwpLeosLldpLocSysCapEnabled_Object=MibScalar
wwpLeosLldpLocSysCapEnabled=_WwpLeosLldpLocSysCapEnabled_Object((1,3,6,1,4,1,6141,2,60,26,1,3,6),_WwpLeosLldpLocSysCapEnabled_Type())
wwpLeosLldpLocSysCapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocSysCapEnabled.setStatus(_A)
_WwpLeosLldpLocPortTable_Object=MibTable
wwpLeosLldpLocPortTable=_WwpLeosLldpLocPortTable_Object((1,3,6,1,4,1,6141,2,60,26,1,3,7))
if mibBuilder.loadTexts:wwpLeosLldpLocPortTable.setStatus(_A)
_WwpLeosLldpLocPortEntry_Object=MibTableRow
wwpLeosLldpLocPortEntry=_WwpLeosLldpLocPortEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,3,7,1))
wwpLeosLldpLocPortEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:wwpLeosLldpLocPortEntry.setStatus(_A)
_WwpLeosLldpLocPortNum_Type=WwpLeosLldpPortNumber
_WwpLeosLldpLocPortNum_Object=MibTableColumn
wwpLeosLldpLocPortNum=_WwpLeosLldpLocPortNum_Object((1,3,6,1,4,1,6141,2,60,26,1,3,7,1,1),_WwpLeosLldpLocPortNum_Type())
wwpLeosLldpLocPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpLocPortNum.setStatus(_A)
_WwpLeosLldpLocPortType_Type=WwpLeosLldpPortIdType
_WwpLeosLldpLocPortType_Object=MibTableColumn
wwpLeosLldpLocPortType=_WwpLeosLldpLocPortType_Object((1,3,6,1,4,1,6141,2,60,26,1,3,7,1,2),_WwpLeosLldpLocPortType_Type())
wwpLeosLldpLocPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocPortType.setStatus(_A)
_WwpLeosLldpLocPortId_Type=WwpLeosLldpPortId
_WwpLeosLldpLocPortId_Object=MibTableColumn
wwpLeosLldpLocPortId=_WwpLeosLldpLocPortId_Object((1,3,6,1,4,1,6141,2,60,26,1,3,7,1,3),_WwpLeosLldpLocPortId_Type())
wwpLeosLldpLocPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocPortId.setStatus(_A)
class _WwpLeosLldpLocPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpLeosLldpLocPortDesc_Type.__name__=_G
_WwpLeosLldpLocPortDesc_Object=MibTableColumn
wwpLeosLldpLocPortDesc=_WwpLeosLldpLocPortDesc_Object((1,3,6,1,4,1,6141,2,60,26,1,3,7,1,4),_WwpLeosLldpLocPortDesc_Type())
wwpLeosLldpLocPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocPortDesc.setStatus(_A)
_WwpLeosLldpLocManAddrTable_Object=MibTable
wwpLeosLldpLocManAddrTable=_WwpLeosLldpLocManAddrTable_Object((1,3,6,1,4,1,6141,2,60,26,1,3,8))
if mibBuilder.loadTexts:wwpLeosLldpLocManAddrTable.setStatus(_A)
_WwpLeosLldpLocManAddrEntry_Object=MibTableRow
wwpLeosLldpLocManAddrEntry=_WwpLeosLldpLocManAddrEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,3,8,1))
wwpLeosLldpLocManAddrEntry.setIndexNames((0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:wwpLeosLldpLocManAddrEntry.setStatus(_A)
_WwpLeosLldpLocManAddrType_Type=AddressFamilyNumbers
_WwpLeosLldpLocManAddrType_Object=MibTableColumn
wwpLeosLldpLocManAddrType=_WwpLeosLldpLocManAddrType_Object((1,3,6,1,4,1,6141,2,60,26,1,3,8,1,1),_WwpLeosLldpLocManAddrType_Type())
wwpLeosLldpLocManAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpLocManAddrType.setStatus(_A)
_WwpLeosLldpLocManAddr_Type=WwpLeosLldpManAddress
_WwpLeosLldpLocManAddr_Object=MibTableColumn
wwpLeosLldpLocManAddr=_WwpLeosLldpLocManAddr_Object((1,3,6,1,4,1,6141,2,60,26,1,3,8,1,2),_WwpLeosLldpLocManAddr_Type())
wwpLeosLldpLocManAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpLocManAddr.setStatus(_A)
_WwpLeosLldpLocManAddrLen_Type=Integer32
_WwpLeosLldpLocManAddrLen_Object=MibTableColumn
wwpLeosLldpLocManAddrLen=_WwpLeosLldpLocManAddrLen_Object((1,3,6,1,4,1,6141,2,60,26,1,3,8,1,3),_WwpLeosLldpLocManAddrLen_Type())
wwpLeosLldpLocManAddrLen.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpLocManAddrLen.setStatus(_A)
_WwpLeosLldpLocManAddrIfSubtype_Type=WwpLeosLldpManAddrIfSubtype
_WwpLeosLldpLocManAddrIfSubtype_Object=MibTableColumn
wwpLeosLldpLocManAddrIfSubtype=_WwpLeosLldpLocManAddrIfSubtype_Object((1,3,6,1,4,1,6141,2,60,26,1,3,8,1,4),_WwpLeosLldpLocManAddrIfSubtype_Type())
wwpLeosLldpLocManAddrIfSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocManAddrIfSubtype.setStatus(_A)
_WwpLeosLldpLocManAddrIfId_Type=Integer32
_WwpLeosLldpLocManAddrIfId_Object=MibTableColumn
wwpLeosLldpLocManAddrIfId=_WwpLeosLldpLocManAddrIfId_Object((1,3,6,1,4,1,6141,2,60,26,1,3,8,1,5),_WwpLeosLldpLocManAddrIfId_Type())
wwpLeosLldpLocManAddrIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocManAddrIfId.setStatus(_A)
_WwpLeosLldpLocManAddrOID_Type=ObjectIdentifier
_WwpLeosLldpLocManAddrOID_Object=MibTableColumn
wwpLeosLldpLocManAddrOID=_WwpLeosLldpLocManAddrOID_Object((1,3,6,1,4,1,6141,2,60,26,1,3,8,1,6),_WwpLeosLldpLocManAddrOID_Type())
wwpLeosLldpLocManAddrOID.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpLocManAddrOID.setStatus(_A)
_WwpLeosLldpRemoteSystemsData_ObjectIdentity=ObjectIdentity
wwpLeosLldpRemoteSystemsData=_WwpLeosLldpRemoteSystemsData_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,1,4))
_WwpLeosLldpRemTable_Object=MibTable
wwpLeosLldpRemTable=_WwpLeosLldpRemTable_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1))
if mibBuilder.loadTexts:wwpLeosLldpRemTable.setStatus(_A)
_WwpLeosLldpRemEntry_Object=MibTableRow
wwpLeosLldpRemEntry=_WwpLeosLldpRemEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1))
wwpLeosLldpRemEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:wwpLeosLldpRemEntry.setStatus(_A)
_WwpLeosLldpRemTimeMark_Type=TimeFilter
_WwpLeosLldpRemTimeMark_Object=MibTableColumn
wwpLeosLldpRemTimeMark=_WwpLeosLldpRemTimeMark_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,1),_WwpLeosLldpRemTimeMark_Type())
wwpLeosLldpRemTimeMark.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemTimeMark.setStatus(_A)
_WwpLeosLldpRemLocalPortNum_Type=WwpLeosLldpPortNumber
_WwpLeosLldpRemLocalPortNum_Object=MibTableColumn
wwpLeosLldpRemLocalPortNum=_WwpLeosLldpRemLocalPortNum_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,2),_WwpLeosLldpRemLocalPortNum_Type())
wwpLeosLldpRemLocalPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemLocalPortNum.setStatus(_A)
class _WwpLeosLldpRemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpLeosLldpRemIndex_Type.__name__=_E
_WwpLeosLldpRemIndex_Object=MibTableColumn
wwpLeosLldpRemIndex=_WwpLeosLldpRemIndex_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,3),_WwpLeosLldpRemIndex_Type())
wwpLeosLldpRemIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemIndex.setStatus(_A)
_WwpLeosLldpRemRemoteChassisType_Type=WwpLeosLldpChassisIdType
_WwpLeosLldpRemRemoteChassisType_Object=MibTableColumn
wwpLeosLldpRemRemoteChassisType=_WwpLeosLldpRemRemoteChassisType_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,4),_WwpLeosLldpRemRemoteChassisType_Type())
wwpLeosLldpRemRemoteChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemRemoteChassisType.setStatus(_A)
_WwpLeosLldpRemRemoteChassis_Type=WwpLeosLldpChassisId
_WwpLeosLldpRemRemoteChassis_Object=MibTableColumn
wwpLeosLldpRemRemoteChassis=_WwpLeosLldpRemRemoteChassis_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,5),_WwpLeosLldpRemRemoteChassis_Type())
wwpLeosLldpRemRemoteChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemRemoteChassis.setStatus(_A)
_WwpLeosLldpRemRemotePortType_Type=WwpLeosLldpPortIdType
_WwpLeosLldpRemRemotePortType_Object=MibTableColumn
wwpLeosLldpRemRemotePortType=_WwpLeosLldpRemRemotePortType_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,6),_WwpLeosLldpRemRemotePortType_Type())
wwpLeosLldpRemRemotePortType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemRemotePortType.setStatus(_A)
_WwpLeosLldpRemRemotePort_Type=WwpLeosLldpPortId
_WwpLeosLldpRemRemotePort_Object=MibTableColumn
wwpLeosLldpRemRemotePort=_WwpLeosLldpRemRemotePort_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,7),_WwpLeosLldpRemRemotePort_Type())
wwpLeosLldpRemRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemRemotePort.setStatus(_A)
class _WwpLeosLldpRemPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpLeosLldpRemPortDesc_Type.__name__=_G
_WwpLeosLldpRemPortDesc_Object=MibTableColumn
wwpLeosLldpRemPortDesc=_WwpLeosLldpRemPortDesc_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,8),_WwpLeosLldpRemPortDesc_Type())
wwpLeosLldpRemPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemPortDesc.setStatus(_A)
class _WwpLeosLldpRemSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpLeosLldpRemSysName_Type.__name__=_G
_WwpLeosLldpRemSysName_Object=MibTableColumn
wwpLeosLldpRemSysName=_WwpLeosLldpRemSysName_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,9),_WwpLeosLldpRemSysName_Type())
wwpLeosLldpRemSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemSysName.setStatus(_A)
class _WwpLeosLldpRemSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpLeosLldpRemSysDesc_Type.__name__=_G
_WwpLeosLldpRemSysDesc_Object=MibTableColumn
wwpLeosLldpRemSysDesc=_WwpLeosLldpRemSysDesc_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,10),_WwpLeosLldpRemSysDesc_Type())
wwpLeosLldpRemSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemSysDesc.setStatus(_A)
_WwpLeosLldpRemSysCapSupported_Type=WwpLeosLldpSystemCapabilitiesMap
_WwpLeosLldpRemSysCapSupported_Object=MibTableColumn
wwpLeosLldpRemSysCapSupported=_WwpLeosLldpRemSysCapSupported_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,11),_WwpLeosLldpRemSysCapSupported_Type())
wwpLeosLldpRemSysCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemSysCapSupported.setStatus(_A)
_WwpLeosLldpRemSysCapEnabled_Type=WwpLeosLldpSystemCapabilitiesMap
_WwpLeosLldpRemSysCapEnabled_Object=MibTableColumn
wwpLeosLldpRemSysCapEnabled=_WwpLeosLldpRemSysCapEnabled_Object((1,3,6,1,4,1,6141,2,60,26,1,4,1,1,12),_WwpLeosLldpRemSysCapEnabled_Type())
wwpLeosLldpRemSysCapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemSysCapEnabled.setStatus(_A)
_WwpLeosLldpRemManAddrTable_Object=MibTable
wwpLeosLldpRemManAddrTable=_WwpLeosLldpRemManAddrTable_Object((1,3,6,1,4,1,6141,2,60,26,1,4,2))
if mibBuilder.loadTexts:wwpLeosLldpRemManAddrTable.setStatus(_A)
_WwpLeosLldpRemManAddrEntry_Object=MibTableRow
wwpLeosLldpRemManAddrEntry=_WwpLeosLldpRemManAddrEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,4,2,1))
wwpLeosLldpRemManAddrEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:wwpLeosLldpRemManAddrEntry.setStatus(_A)
_WwpLeosLldpRemManAddrType_Type=AddressFamilyNumbers
_WwpLeosLldpRemManAddrType_Object=MibTableColumn
wwpLeosLldpRemManAddrType=_WwpLeosLldpRemManAddrType_Object((1,3,6,1,4,1,6141,2,60,26,1,4,2,1,1),_WwpLeosLldpRemManAddrType_Type())
wwpLeosLldpRemManAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemManAddrType.setStatus(_A)
_WwpLeosLldpRemManAddr_Type=WwpLeosLldpManAddress
_WwpLeosLldpRemManAddr_Object=MibTableColumn
wwpLeosLldpRemManAddr=_WwpLeosLldpRemManAddr_Object((1,3,6,1,4,1,6141,2,60,26,1,4,2,1,2),_WwpLeosLldpRemManAddr_Type())
wwpLeosLldpRemManAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemManAddr.setStatus(_A)
_WwpLeosLldpRemManAddrIfSubtype_Type=WwpLeosLldpManAddrIfSubtype
_WwpLeosLldpRemManAddrIfSubtype_Object=MibTableColumn
wwpLeosLldpRemManAddrIfSubtype=_WwpLeosLldpRemManAddrIfSubtype_Object((1,3,6,1,4,1,6141,2,60,26,1,4,2,1,3),_WwpLeosLldpRemManAddrIfSubtype_Type())
wwpLeosLldpRemManAddrIfSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemManAddrIfSubtype.setStatus(_A)
_WwpLeosLldpRemManAddrIfId_Type=Integer32
_WwpLeosLldpRemManAddrIfId_Object=MibTableColumn
wwpLeosLldpRemManAddrIfId=_WwpLeosLldpRemManAddrIfId_Object((1,3,6,1,4,1,6141,2,60,26,1,4,2,1,4),_WwpLeosLldpRemManAddrIfId_Type())
wwpLeosLldpRemManAddrIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemManAddrIfId.setStatus(_A)
_WwpLeosLldpRemManAddrOID_Type=ObjectIdentifier
_WwpLeosLldpRemManAddrOID_Object=MibTableColumn
wwpLeosLldpRemManAddrOID=_WwpLeosLldpRemManAddrOID_Object((1,3,6,1,4,1,6141,2,60,26,1,4,2,1,5),_WwpLeosLldpRemManAddrOID_Type())
wwpLeosLldpRemManAddrOID.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemManAddrOID.setStatus(_A)
_WwpLeosLldpRemUnknownTLVTable_Object=MibTable
wwpLeosLldpRemUnknownTLVTable=_WwpLeosLldpRemUnknownTLVTable_Object((1,3,6,1,4,1,6141,2,60,26,1,4,3))
if mibBuilder.loadTexts:wwpLeosLldpRemUnknownTLVTable.setStatus(_A)
_WwpLeosLldpRemUnknownTLVEntry_Object=MibTableRow
wwpLeosLldpRemUnknownTLVEntry=_WwpLeosLldpRemUnknownTLVEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,4,3,1))
wwpLeosLldpRemUnknownTLVEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:wwpLeosLldpRemUnknownTLVEntry.setStatus(_A)
class _WwpLeosLldpRemUnknownTLVType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9,126))
_WwpLeosLldpRemUnknownTLVType_Type.__name__=_E
_WwpLeosLldpRemUnknownTLVType_Object=MibTableColumn
wwpLeosLldpRemUnknownTLVType=_WwpLeosLldpRemUnknownTLVType_Object((1,3,6,1,4,1,6141,2,60,26,1,4,3,1,1),_WwpLeosLldpRemUnknownTLVType_Type())
wwpLeosLldpRemUnknownTLVType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemUnknownTLVType.setStatus(_A)
class _WwpLeosLldpRemUnknownTLVInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_WwpLeosLldpRemUnknownTLVInfo_Type.__name__=_L
_WwpLeosLldpRemUnknownTLVInfo_Object=MibTableColumn
wwpLeosLldpRemUnknownTLVInfo=_WwpLeosLldpRemUnknownTLVInfo_Object((1,3,6,1,4,1,6141,2,60,26,1,4,3,1,2),_WwpLeosLldpRemUnknownTLVInfo_Type())
wwpLeosLldpRemUnknownTLVInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemUnknownTLVInfo.setStatus(_A)
_WwpLeosLldpRemOrgDefInfoTable_Object=MibTable
wwpLeosLldpRemOrgDefInfoTable=_WwpLeosLldpRemOrgDefInfoTable_Object((1,3,6,1,4,1,6141,2,60,26,1,4,4))
if mibBuilder.loadTexts:wwpLeosLldpRemOrgDefInfoTable.setStatus(_A)
_WwpLeosLldpRemOrgDefInfoEntry_Object=MibTableRow
wwpLeosLldpRemOrgDefInfoEntry=_WwpLeosLldpRemOrgDefInfoEntry_Object((1,3,6,1,4,1,6141,2,60,26,1,4,4,1))
wwpLeosLldpRemOrgDefInfoEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_Z),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:wwpLeosLldpRemOrgDefInfoEntry.setStatus(_A)
class _WwpLeosLldpRemOrgDefInfoOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WwpLeosLldpRemOrgDefInfoOUI_Type.__name__=_L
_WwpLeosLldpRemOrgDefInfoOUI_Object=MibTableColumn
wwpLeosLldpRemOrgDefInfoOUI=_WwpLeosLldpRemOrgDefInfoOUI_Object((1,3,6,1,4,1,6141,2,60,26,1,4,4,1,1),_WwpLeosLldpRemOrgDefInfoOUI_Type())
wwpLeosLldpRemOrgDefInfoOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemOrgDefInfoOUI.setStatus(_A)
class _WwpLeosLldpRemOrgDefInfoSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WwpLeosLldpRemOrgDefInfoSubtype_Type.__name__=_E
_WwpLeosLldpRemOrgDefInfoSubtype_Object=MibTableColumn
wwpLeosLldpRemOrgDefInfoSubtype=_WwpLeosLldpRemOrgDefInfoSubtype_Object((1,3,6,1,4,1,6141,2,60,26,1,4,4,1,2),_WwpLeosLldpRemOrgDefInfoSubtype_Type())
wwpLeosLldpRemOrgDefInfoSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemOrgDefInfoSubtype.setStatus(_A)
class _WwpLeosLldpRemOrgDefInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpLeosLldpRemOrgDefInfoIndex_Type.__name__=_E
_WwpLeosLldpRemOrgDefInfoIndex_Object=MibTableColumn
wwpLeosLldpRemOrgDefInfoIndex=_WwpLeosLldpRemOrgDefInfoIndex_Object((1,3,6,1,4,1,6141,2,60,26,1,4,4,1,3),_WwpLeosLldpRemOrgDefInfoIndex_Type())
wwpLeosLldpRemOrgDefInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLldpRemOrgDefInfoIndex.setStatus(_A)
class _WwpLeosLldpRemOrgDefInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,507))
_WwpLeosLldpRemOrgDefInfo_Type.__name__=_L
_WwpLeosLldpRemOrgDefInfo_Object=MibTableColumn
wwpLeosLldpRemOrgDefInfo=_WwpLeosLldpRemOrgDefInfo_Object((1,3,6,1,4,1,6141,2,60,26,1,4,4,1,4),_WwpLeosLldpRemOrgDefInfo_Type())
wwpLeosLldpRemOrgDefInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLldpRemOrgDefInfo.setStatus(_A)
_WwpLeosLldpExtentions_ObjectIdentity=ObjectIdentity
wwpLeosLldpExtentions=_WwpLeosLldpExtentions_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,1,5))
_WwpLeosLldpGlobalAtts_ObjectIdentity=ObjectIdentity
wwpLeosLldpGlobalAtts=_WwpLeosLldpGlobalAtts_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,1,6))
_WwpLeosLldpStatsClear_Type=TruthValue
_WwpLeosLldpStatsClear_Object=MibScalar
wwpLeosLldpStatsClear=_WwpLeosLldpStatsClear_Object((1,3,6,1,4,1,6141,2,60,26,1,6,1),_WwpLeosLldpStatsClear_Type())
wwpLeosLldpStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosLldpStatsClear.setStatus(_H)
_WwpLeosLldpConformance_ObjectIdentity=ObjectIdentity
wwpLeosLldpConformance=_WwpLeosLldpConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,2))
_WwpLeosLldpCompliances_ObjectIdentity=ObjectIdentity
wwpLeosLldpCompliances=_WwpLeosLldpCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,2,1))
_WwpLeosLldpGroups_ObjectIdentity=ObjectIdentity
wwpLeosLldpGroups=_WwpLeosLldpGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,2,2))
_WwpLeosLldpNotifMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosLldpNotifMIBNotificationPrefix=_WwpLeosLldpNotifMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,3))
_WwpLeosLldpNotifMIBNotification_ObjectIdentity=ObjectIdentity
wwpLeosLldpNotifMIBNotification=_WwpLeosLldpNotifMIBNotification_ObjectIdentity((1,3,6,1,4,1,6141,2,60,26,3,0))
wwpLeosLldpLocManAddrEntry.registerAugmentions((_B,_c))
wwpLeosLldpConfigManAddrEntry.setIndexNames(*wwpLeosLldpLocManAddrEntry.getIndexNames())
wwpLeosLldpConfigGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,26,2,2,1))
wwpLeosLldpConfigGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:wwpLeosLldpConfigGroup.setStatus(_A)
wwpLeosLldpStatsGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,26,2,2,2))
wwpLeosLldpStatsGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:wwpLeosLldpStatsGroup.setStatus(_A)
wwpLeosLldpLocSysGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,26,2,2,3))
wwpLeosLldpLocSysGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:wwpLeosLldpLocSysGroup.setStatus(_A)
wwpLeosLldpOptLocSysGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,26,2,2,4))
wwpLeosLldpOptLocSysGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:wwpLeosLldpOptLocSysGroup.setStatus(_A)
wwpLeosLldpRemSysGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,26,2,2,5))
wwpLeosLldpRemSysGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:wwpLeosLldpRemSysGroup.setStatus(_A)
wwpLeosLldpPortSpeedChangeTrap=NotificationType((1,3,6,1,4,1,6141,2,60,26,3,0,1))
wwpLeosLldpPortSpeedChangeTrap.setObjects(*((_B,_N),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:wwpLeosLldpPortSpeedChangeTrap.setStatus(_H)
wwpLeosLldpCompliance=ModuleCompliance((1,3,6,1,4,1,6141,2,60,26,2,1,1))
wwpLeosLldpCompliance.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:wwpLeosLldpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TimeFilter':TimeFilter,_G:SnmpAdminString,'WwpLeosLldpChassisIdType':WwpLeosLldpChassisIdType,'WwpLeosLldpChassisId':WwpLeosLldpChassisId,'WwpLeosLldpPortIdType':WwpLeosLldpPortIdType,'WwpLeosLldpPortId':WwpLeosLldpPortId,'WwpLeosLldpManAddrIfSubtype':WwpLeosLldpManAddrIfSubtype,'WwpLeosLldpManAddress':WwpLeosLldpManAddress,'WwpLeosLldpSystemCapabilitiesMap':WwpLeosLldpSystemCapabilitiesMap,'WwpLeosLldpPortNumber':WwpLeosLldpPortNumber,'WwpLeosLldpPortList':WwpLeosLldpPortList,'wwpLeosLldpMIB':wwpLeosLldpMIB,'wwpLeosLldpMIBObjects':wwpLeosLldpMIBObjects,'wwpLeosLldpConfiguration':wwpLeosLldpConfiguration,_d:wwpLeosLldpMessageTxInterval,_e:wwpLeosLldpMessageTxHoldMultiplier,_f:wwpLeosLldpReinitDelay,_g:wwpLeosLldpTxDelay,'wwpLeosLldpPortConfigTable':wwpLeosLldpPortConfigTable,'wwpLeosLldpPortConfigEntry':wwpLeosLldpPortConfigEntry,_N:wwpLeosLldpPortConfigPortNum,_h:wwpLeosLldpPortConfigAdminStatus,_i:wwpLeosLldpPortConfigTLVsTxEnable,'wwpLeosLldpPortConfigStatsClear':wwpLeosLldpPortConfigStatsClear,_AI:wwpLeosLldpPortConfigOperPortSpeed,_AJ:wwpLeosLldpPortConfigReqPortSpeed,'wwpLeosLldpConfigManAddrTable':wwpLeosLldpConfigManAddrTable,_c:wwpLeosLldpConfigManAddrEntry,_j:wwpLeosLldpManAddrPortsTxEnable,'wwpLeosLldpStatistics':wwpLeosLldpStatistics,'wwpLeosLldpStatsTable':wwpLeosLldpStatsTable,'wwpLeosLldpStatsEntry':wwpLeosLldpStatsEntry,_T:wwpLeosLldpStatsPortNum,_k:wwpLeosLldpStatsFramesDiscardedTotal,_l:wwpLeosLldpStatsFramesInErrors,_m:wwpLeosLldpStatsFramesInTotal,_n:wwpLeosLldpStatsFramesOutTotal,_o:wwpLeosLldpStatsTLVsInErrors,_p:wwpLeosLldpStatsTLVsDiscardedTotal,_q:wwpLeosLldpStatsTLVsUnrecognizedTotal,_r:wwpLeosLldpCounterDiscontinuityTime,'wwpLeosLldpLocalSystemData':wwpLeosLldpLocalSystemData,_s:wwpLeosLldpLocChassisType,_t:wwpLeosLldpLocChassisId,_y:wwpLeosLldpLocSysName,_x:wwpLeosLldpLocSysDesc,_z:wwpLeosLldpLocSysCapSupported,_A0:wwpLeosLldpLocSysCapEnabled,'wwpLeosLldpLocPortTable':wwpLeosLldpLocPortTable,'wwpLeosLldpLocPortEntry':wwpLeosLldpLocPortEntry,_U:wwpLeosLldpLocPortNum,_u:wwpLeosLldpLocPortType,_v:wwpLeosLldpLocPortId,_w:wwpLeosLldpLocPortDesc,'wwpLeosLldpLocManAddrTable':wwpLeosLldpLocManAddrTable,'wwpLeosLldpLocManAddrEntry':wwpLeosLldpLocManAddrEntry,_V:wwpLeosLldpLocManAddrType,_W:wwpLeosLldpLocManAddr,'wwpLeosLldpLocManAddrLen':wwpLeosLldpLocManAddrLen,_A1:wwpLeosLldpLocManAddrIfSubtype,_A2:wwpLeosLldpLocManAddrIfId,_A3:wwpLeosLldpLocManAddrOID,'wwpLeosLldpRemoteSystemsData':wwpLeosLldpRemoteSystemsData,'wwpLeosLldpRemTable':wwpLeosLldpRemTable,'wwpLeosLldpRemEntry':wwpLeosLldpRemEntry,_I:wwpLeosLldpRemTimeMark,_J:wwpLeosLldpRemLocalPortNum,_K:wwpLeosLldpRemIndex,_A4:wwpLeosLldpRemRemoteChassisType,_A5:wwpLeosLldpRemRemoteChassis,_A6:wwpLeosLldpRemRemotePortType,_A7:wwpLeosLldpRemRemotePort,_A8:wwpLeosLldpRemPortDesc,_A9:wwpLeosLldpRemSysName,_AA:wwpLeosLldpRemSysDesc,_AB:wwpLeosLldpRemSysCapSupported,_AC:wwpLeosLldpRemSysCapEnabled,'wwpLeosLldpRemManAddrTable':wwpLeosLldpRemManAddrTable,'wwpLeosLldpRemManAddrEntry':wwpLeosLldpRemManAddrEntry,_X:wwpLeosLldpRemManAddrType,_Y:wwpLeosLldpRemManAddr,_AD:wwpLeosLldpRemManAddrIfSubtype,_AE:wwpLeosLldpRemManAddrIfId,_AF:wwpLeosLldpRemManAddrOID,'wwpLeosLldpRemUnknownTLVTable':wwpLeosLldpRemUnknownTLVTable,'wwpLeosLldpRemUnknownTLVEntry':wwpLeosLldpRemUnknownTLVEntry,'wwpLeosLldpRemUnknownTLVType':wwpLeosLldpRemUnknownTLVType,_AG:wwpLeosLldpRemUnknownTLVInfo,'wwpLeosLldpRemOrgDefInfoTable':wwpLeosLldpRemOrgDefInfoTable,'wwpLeosLldpRemOrgDefInfoEntry':wwpLeosLldpRemOrgDefInfoEntry,_Z:wwpLeosLldpRemOrgDefInfoOUI,_a:wwpLeosLldpRemOrgDefInfoSubtype,_b:wwpLeosLldpRemOrgDefInfoIndex,_AH:wwpLeosLldpRemOrgDefInfo,'wwpLeosLldpExtentions':wwpLeosLldpExtentions,'wwpLeosLldpGlobalAtts':wwpLeosLldpGlobalAtts,'wwpLeosLldpStatsClear':wwpLeosLldpStatsClear,'wwpLeosLldpConformance':wwpLeosLldpConformance,'wwpLeosLldpCompliances':wwpLeosLldpCompliances,'wwpLeosLldpCompliance':wwpLeosLldpCompliance,'wwpLeosLldpGroups':wwpLeosLldpGroups,_AK:wwpLeosLldpConfigGroup,_AL:wwpLeosLldpStatsGroup,_AM:wwpLeosLldpLocSysGroup,_AO:wwpLeosLldpOptLocSysGroup,_AN:wwpLeosLldpRemSysGroup,'wwpLeosLldpNotifMIBNotificationPrefix':wwpLeosLldpNotifMIBNotificationPrefix,'wwpLeosLldpNotifMIBNotification':wwpLeosLldpNotifMIBNotification,'wwpLeosLldpPortSpeedChangeTrap':wwpLeosLldpPortSpeedChangeTrap})