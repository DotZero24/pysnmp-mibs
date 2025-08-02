_Ab='lldpNotificationsGroup'
_Aa='lldpRemSysGroup'
_AZ='lldpLocSysGroup'
_AY='lldpStatsTxGroup'
_AX='lldpStatsRxGroup'
_AW='lldpConfigTxGroup'
_AV='lldpConfigRxGroup'
_AU='lldpConfigGroup'
_AT='lldpRemTablesChange'
_AS='lldpRemOrgDefInfo'
_AR='lldpRemUnknownTLVInfo'
_AQ='lldpRemManAddrOID'
_AP='lldpRemManAddrIfId'
_AO='lldpRemManAddrIfSubtype'
_AN='lldpRemSysCapEnabled'
_AM='lldpRemSysCapSupported'
_AL='lldpRemSysDesc'
_AK='lldpRemSysName'
_AJ='lldpRemPortDesc'
_AI='lldpRemPortId'
_AH='lldpRemPortIdSubtype'
_AG='lldpRemChassisId'
_AF='lldpRemChassisIdSubtype'
_AE='lldpLocManAddrOID'
_AD='lldpLocManAddrIfId'
_AC='lldpLocManAddrIfSubtype'
_AB='lldpLocManAddrLen'
_AA='lldpLocSysCapEnabled'
_A9='lldpLocSysCapSupported'
_A8='lldpLocSysName'
_A7='lldpLocSysDesc'
_A6='lldpLocPortDesc'
_A5='lldpLocPortId'
_A4='lldpLocPortIdSubtype'
_A3='lldpLocChassisId'
_A2='lldpLocChassisIdSubtype'
_A1='lldpStatsTxPortFramesTotal'
_A0='lldpStatsRxPortAgeoutsTotal'
_z='lldpStatsRxPortTLVsUnrecognizedTotal'
_y='lldpStatsRxPortTLVsDiscardedTotal'
_x='lldpStatsRxPortFramesTotal'
_w='lldpStatsRxPortFramesErrors'
_v='lldpStatsRxPortFramesDiscardedTotal'
_u='lldpStatsRemTablesLastChangeTime'
_t='lldpConfigManAddrPortsTxEnable'
_s='lldpPortConfigTLVsTxEnable'
_r='lldpTxDelay'
_q='lldpReinitDelay'
_p='lldpMessageTxHoldMultiplier'
_o='lldpMessageTxInterval'
_n='lldpPortConfigNotificationEnable'
_m='lldpNotificationInterval'
_l='lldpPortConfigAdminStatus'
_k='lldpConfigManAddrEntry'
_j='lldpRemOrgDefInfoIndex'
_i='lldpRemOrgDefInfoSubtype'
_h='lldpRemOrgDefInfoOUI'
_g='lldpRemUnknownTLVType'
_f='lldpRemManAddr'
_e='lldpRemManAddrSubtype'
_d='lldpLocManAddr'
_c='lldpLocManAddrSubtype'
_b='lldpLocPortNum'
_a='lldpStatsRxPortNum'
_Z='lldpStatsTxPortNum'
_Y='LldpPortList'
_X='lldpPortConfigPortNum'
_W='interfaceName'
_V='networkAddress'
_U='macAddress'
_T='portComponent'
_S='interfaceAlias'
_R='TruthValue'
_Q='lldpStatsRemTablesAgeouts'
_P='lldpStatsRemTablesDrops'
_O='lldpStatsRemTablesDeletes'
_N='lldpStatsRemTablesInserts'
_M='table entries'
_L='seconds'
_K='OctetString'
_J='lldpRemIndex'
_I='lldpRemLocalPortNum'
_H='lldpRemTimeMark'
_G='SnmpAdminString'
_F='read-write'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='FS-NMS-LLDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nms,=mibBuilder.importSymbols('FS-NMS-SMI','nms')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_R)
nmslldpMIB=ModuleIdentity((1,3,6,1,4,1,52642,127))
if mibBuilder.loadTexts:nmslldpMIB.setRevisions(('2004-11-22 00:00',))
class TimeFilter(TextualConvention,TimeTicks):status=_A
class ZeroBasedCounter32(TextualConvention,Gauge32):status=_A
class LldpChassisIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('chassisComponent',1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6),('local',7)))
class LldpChassisId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class LldpPortIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_V,4),(_W,5),('agentCircuitId',6),('local',7)))
class LldpPortId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class LldpManAddrIfSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('ifIndex',2),('systemPortNumber',3)))
class LldpManAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class LldpSystemCapabilitiesMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('other',0),('repeater',1),('bridge',2),('wlanAccessPoint',3),('router',4),('telephone',5),('docsisCableDevice',6),('stationOnly',7)))
class LldpPortNumber(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
class LldpPortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_LldpNotifications_ObjectIdentity=ObjectIdentity
lldpNotifications=_LldpNotifications_ObjectIdentity((1,3,6,1,4,1,52642,127,0))
_LldpNotificationPrefix_ObjectIdentity=ObjectIdentity
lldpNotificationPrefix=_LldpNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,52642,127,0,0))
_LldpObjects_ObjectIdentity=ObjectIdentity
lldpObjects=_LldpObjects_ObjectIdentity((1,3,6,1,4,1,52642,127,1))
_LldpConfiguration_ObjectIdentity=ObjectIdentity
lldpConfiguration=_LldpConfiguration_ObjectIdentity((1,3,6,1,4,1,52642,127,1,1))
class _LldpMessageTxInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,32768))
_LldpMessageTxInterval_Type.__name__=_E
_LldpMessageTxInterval_Object=MibScalar
lldpMessageTxInterval=_LldpMessageTxInterval_Object((1,3,6,1,4,1,52642,127,1,1,1),_LldpMessageTxInterval_Type())
lldpMessageTxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpMessageTxInterval.setStatus(_A)
if mibBuilder.loadTexts:lldpMessageTxInterval.setUnits(_L)
class _LldpMessageTxHoldMultiplier_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_LldpMessageTxHoldMultiplier_Type.__name__=_E
_LldpMessageTxHoldMultiplier_Object=MibScalar
lldpMessageTxHoldMultiplier=_LldpMessageTxHoldMultiplier_Object((1,3,6,1,4,1,52642,127,1,1,2),_LldpMessageTxHoldMultiplier_Type())
lldpMessageTxHoldMultiplier.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpMessageTxHoldMultiplier.setStatus(_A)
class _LldpReinitDelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LldpReinitDelay_Type.__name__=_E
_LldpReinitDelay_Object=MibScalar
lldpReinitDelay=_LldpReinitDelay_Object((1,3,6,1,4,1,52642,127,1,1,3),_LldpReinitDelay_Type())
lldpReinitDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpReinitDelay.setStatus(_A)
if mibBuilder.loadTexts:lldpReinitDelay.setUnits(_L)
class _LldpTxDelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_LldpTxDelay_Type.__name__=_E
_LldpTxDelay_Object=MibScalar
lldpTxDelay=_LldpTxDelay_Object((1,3,6,1,4,1,52642,127,1,1,4),_LldpTxDelay_Type())
lldpTxDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpTxDelay.setStatus(_A)
if mibBuilder.loadTexts:lldpTxDelay.setUnits(_L)
class _LldpNotificationInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_LldpNotificationInterval_Type.__name__=_E
_LldpNotificationInterval_Object=MibScalar
lldpNotificationInterval=_LldpNotificationInterval_Object((1,3,6,1,4,1,52642,127,1,1,5),_LldpNotificationInterval_Type())
lldpNotificationInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:lldpNotificationInterval.setUnits(_L)
_LldpPortConfigTable_Object=MibTable
lldpPortConfigTable=_LldpPortConfigTable_Object((1,3,6,1,4,1,52642,127,1,1,6))
if mibBuilder.loadTexts:lldpPortConfigTable.setStatus(_A)
_LldpPortConfigEntry_Object=MibTableRow
lldpPortConfigEntry=_LldpPortConfigEntry_Object((1,3,6,1,4,1,52642,127,1,1,6,1))
lldpPortConfigEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:lldpPortConfigEntry.setStatus(_A)
_LldpPortConfigPortNum_Type=LldpPortNumber
_LldpPortConfigPortNum_Object=MibTableColumn
lldpPortConfigPortNum=_LldpPortConfigPortNum_Object((1,3,6,1,4,1,52642,127,1,1,6,1,1),_LldpPortConfigPortNum_Type())
lldpPortConfigPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpPortConfigPortNum.setStatus(_A)
class _LldpPortConfigAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('txOnly',1),('rxOnly',2),('txAndRx',3),('disabled',4)))
_LldpPortConfigAdminStatus_Type.__name__=_E
_LldpPortConfigAdminStatus_Object=MibTableColumn
lldpPortConfigAdminStatus=_LldpPortConfigAdminStatus_Object((1,3,6,1,4,1,52642,127,1,1,6,1,2),_LldpPortConfigAdminStatus_Type())
lldpPortConfigAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpPortConfigAdminStatus.setStatus(_A)
class _LldpPortConfigNotificationEnable_Type(TruthValue):defaultValue=2
_LldpPortConfigNotificationEnable_Type.__name__=_R
_LldpPortConfigNotificationEnable_Object=MibTableColumn
lldpPortConfigNotificationEnable=_LldpPortConfigNotificationEnable_Object((1,3,6,1,4,1,52642,127,1,1,6,1,3),_LldpPortConfigNotificationEnable_Type())
lldpPortConfigNotificationEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpPortConfigNotificationEnable.setStatus(_A)
class _LldpPortConfigTLVsTxEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('portDesc',0),('sysName',1),('sysDesc',2),('sysCap',3)))
_LldpPortConfigTLVsTxEnable_Type.__name__='Bits'
_LldpPortConfigTLVsTxEnable_Object=MibTableColumn
lldpPortConfigTLVsTxEnable=_LldpPortConfigTLVsTxEnable_Object((1,3,6,1,4,1,52642,127,1,1,6,1,4),_LldpPortConfigTLVsTxEnable_Type())
lldpPortConfigTLVsTxEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpPortConfigTLVsTxEnable.setStatus(_A)
_LldpConfigManAddrTable_Object=MibTable
lldpConfigManAddrTable=_LldpConfigManAddrTable_Object((1,3,6,1,4,1,52642,127,1,1,7))
if mibBuilder.loadTexts:lldpConfigManAddrTable.setStatus(_A)
_LldpConfigManAddrEntry_Object=MibTableRow
lldpConfigManAddrEntry=_LldpConfigManAddrEntry_Object((1,3,6,1,4,1,52642,127,1,1,7,1))
if mibBuilder.loadTexts:lldpConfigManAddrEntry.setStatus(_A)
class _LldpConfigManAddrPortsTxEnable_Type(LldpPortList):defaultHexValue=''
_LldpConfigManAddrPortsTxEnable_Type.__name__=_Y
_LldpConfigManAddrPortsTxEnable_Object=MibTableColumn
lldpConfigManAddrPortsTxEnable=_LldpConfigManAddrPortsTxEnable_Object((1,3,6,1,4,1,52642,127,1,1,7,1,1),_LldpConfigManAddrPortsTxEnable_Type())
lldpConfigManAddrPortsTxEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpConfigManAddrPortsTxEnable.setStatus(_A)
_LldpStatistics_ObjectIdentity=ObjectIdentity
lldpStatistics=_LldpStatistics_ObjectIdentity((1,3,6,1,4,1,52642,127,1,2))
_LldpStatsRemTablesLastChangeTime_Type=TimeStamp
_LldpStatsRemTablesLastChangeTime_Object=MibScalar
lldpStatsRemTablesLastChangeTime=_LldpStatsRemTablesLastChangeTime_Object((1,3,6,1,4,1,52642,127,1,2,1),_LldpStatsRemTablesLastChangeTime_Type())
lldpStatsRemTablesLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRemTablesLastChangeTime.setStatus(_A)
_LldpStatsRemTablesInserts_Type=ZeroBasedCounter32
_LldpStatsRemTablesInserts_Object=MibScalar
lldpStatsRemTablesInserts=_LldpStatsRemTablesInserts_Object((1,3,6,1,4,1,52642,127,1,2,2),_LldpStatsRemTablesInserts_Type())
lldpStatsRemTablesInserts.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRemTablesInserts.setStatus(_A)
if mibBuilder.loadTexts:lldpStatsRemTablesInserts.setUnits(_M)
_LldpStatsRemTablesDeletes_Type=ZeroBasedCounter32
_LldpStatsRemTablesDeletes_Object=MibScalar
lldpStatsRemTablesDeletes=_LldpStatsRemTablesDeletes_Object((1,3,6,1,4,1,52642,127,1,2,3),_LldpStatsRemTablesDeletes_Type())
lldpStatsRemTablesDeletes.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRemTablesDeletes.setStatus(_A)
if mibBuilder.loadTexts:lldpStatsRemTablesDeletes.setUnits(_M)
_LldpStatsRemTablesDrops_Type=ZeroBasedCounter32
_LldpStatsRemTablesDrops_Object=MibScalar
lldpStatsRemTablesDrops=_LldpStatsRemTablesDrops_Object((1,3,6,1,4,1,52642,127,1,2,4),_LldpStatsRemTablesDrops_Type())
lldpStatsRemTablesDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRemTablesDrops.setStatus(_A)
if mibBuilder.loadTexts:lldpStatsRemTablesDrops.setUnits(_M)
_LldpStatsRemTablesAgeouts_Type=ZeroBasedCounter32
_LldpStatsRemTablesAgeouts_Object=MibScalar
lldpStatsRemTablesAgeouts=_LldpStatsRemTablesAgeouts_Object((1,3,6,1,4,1,52642,127,1,2,5),_LldpStatsRemTablesAgeouts_Type())
lldpStatsRemTablesAgeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRemTablesAgeouts.setStatus(_A)
_LldpStatsTxPortTable_Object=MibTable
lldpStatsTxPortTable=_LldpStatsTxPortTable_Object((1,3,6,1,4,1,52642,127,1,2,6))
if mibBuilder.loadTexts:lldpStatsTxPortTable.setStatus(_A)
_LldpStatsTxPortEntry_Object=MibTableRow
lldpStatsTxPortEntry=_LldpStatsTxPortEntry_Object((1,3,6,1,4,1,52642,127,1,2,6,1))
lldpStatsTxPortEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:lldpStatsTxPortEntry.setStatus(_A)
_LldpStatsTxPortNum_Type=LldpPortNumber
_LldpStatsTxPortNum_Object=MibTableColumn
lldpStatsTxPortNum=_LldpStatsTxPortNum_Object((1,3,6,1,4,1,52642,127,1,2,6,1,1),_LldpStatsTxPortNum_Type())
lldpStatsTxPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpStatsTxPortNum.setStatus(_A)
_LldpStatsTxPortFramesTotal_Type=Counter32
_LldpStatsTxPortFramesTotal_Object=MibTableColumn
lldpStatsTxPortFramesTotal=_LldpStatsTxPortFramesTotal_Object((1,3,6,1,4,1,52642,127,1,2,6,1,2),_LldpStatsTxPortFramesTotal_Type())
lldpStatsTxPortFramesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsTxPortFramesTotal.setStatus(_A)
_LldpStatsRxPortTable_Object=MibTable
lldpStatsRxPortTable=_LldpStatsRxPortTable_Object((1,3,6,1,4,1,52642,127,1,2,7))
if mibBuilder.loadTexts:lldpStatsRxPortTable.setStatus(_A)
_LldpStatsRxPortEntry_Object=MibTableRow
lldpStatsRxPortEntry=_LldpStatsRxPortEntry_Object((1,3,6,1,4,1,52642,127,1,2,7,1))
lldpStatsRxPortEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:lldpStatsRxPortEntry.setStatus(_A)
_LldpStatsRxPortNum_Type=LldpPortNumber
_LldpStatsRxPortNum_Object=MibTableColumn
lldpStatsRxPortNum=_LldpStatsRxPortNum_Object((1,3,6,1,4,1,52642,127,1,2,7,1,1),_LldpStatsRxPortNum_Type())
lldpStatsRxPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpStatsRxPortNum.setStatus(_A)
_LldpStatsRxPortFramesDiscardedTotal_Type=Counter32
_LldpStatsRxPortFramesDiscardedTotal_Object=MibTableColumn
lldpStatsRxPortFramesDiscardedTotal=_LldpStatsRxPortFramesDiscardedTotal_Object((1,3,6,1,4,1,52642,127,1,2,7,1,2),_LldpStatsRxPortFramesDiscardedTotal_Type())
lldpStatsRxPortFramesDiscardedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRxPortFramesDiscardedTotal.setStatus(_A)
_LldpStatsRxPortFramesErrors_Type=Counter32
_LldpStatsRxPortFramesErrors_Object=MibTableColumn
lldpStatsRxPortFramesErrors=_LldpStatsRxPortFramesErrors_Object((1,3,6,1,4,1,52642,127,1,2,7,1,3),_LldpStatsRxPortFramesErrors_Type())
lldpStatsRxPortFramesErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRxPortFramesErrors.setStatus(_A)
_LldpStatsRxPortFramesTotal_Type=Counter32
_LldpStatsRxPortFramesTotal_Object=MibTableColumn
lldpStatsRxPortFramesTotal=_LldpStatsRxPortFramesTotal_Object((1,3,6,1,4,1,52642,127,1,2,7,1,4),_LldpStatsRxPortFramesTotal_Type())
lldpStatsRxPortFramesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRxPortFramesTotal.setStatus(_A)
_LldpStatsRxPortTLVsDiscardedTotal_Type=Counter32
_LldpStatsRxPortTLVsDiscardedTotal_Object=MibTableColumn
lldpStatsRxPortTLVsDiscardedTotal=_LldpStatsRxPortTLVsDiscardedTotal_Object((1,3,6,1,4,1,52642,127,1,2,7,1,5),_LldpStatsRxPortTLVsDiscardedTotal_Type())
lldpStatsRxPortTLVsDiscardedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRxPortTLVsDiscardedTotal.setStatus(_A)
_LldpStatsRxPortTLVsUnrecognizedTotal_Type=Counter32
_LldpStatsRxPortTLVsUnrecognizedTotal_Object=MibTableColumn
lldpStatsRxPortTLVsUnrecognizedTotal=_LldpStatsRxPortTLVsUnrecognizedTotal_Object((1,3,6,1,4,1,52642,127,1,2,7,1,6),_LldpStatsRxPortTLVsUnrecognizedTotal_Type())
lldpStatsRxPortTLVsUnrecognizedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRxPortTLVsUnrecognizedTotal.setStatus(_A)
_LldpStatsRxPortAgeoutsTotal_Type=ZeroBasedCounter32
_LldpStatsRxPortAgeoutsTotal_Object=MibTableColumn
lldpStatsRxPortAgeoutsTotal=_LldpStatsRxPortAgeoutsTotal_Object((1,3,6,1,4,1,52642,127,1,2,7,1,7),_LldpStatsRxPortAgeoutsTotal_Type())
lldpStatsRxPortAgeoutsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpStatsRxPortAgeoutsTotal.setStatus(_A)
_LldpLocalSystemData_ObjectIdentity=ObjectIdentity
lldpLocalSystemData=_LldpLocalSystemData_ObjectIdentity((1,3,6,1,4,1,52642,127,1,3))
_LldpLocChassisIdSubtype_Type=LldpChassisIdSubtype
_LldpLocChassisIdSubtype_Object=MibScalar
lldpLocChassisIdSubtype=_LldpLocChassisIdSubtype_Object((1,3,6,1,4,1,52642,127,1,3,1),_LldpLocChassisIdSubtype_Type())
lldpLocChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocChassisIdSubtype.setStatus(_A)
_LldpLocChassisId_Type=LldpChassisId
_LldpLocChassisId_Object=MibScalar
lldpLocChassisId=_LldpLocChassisId_Object((1,3,6,1,4,1,52642,127,1,3,2),_LldpLocChassisId_Type())
lldpLocChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocChassisId.setStatus(_A)
class _LldpLocSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocSysName_Type.__name__=_G
_LldpLocSysName_Object=MibScalar
lldpLocSysName=_LldpLocSysName_Object((1,3,6,1,4,1,52642,127,1,3,3),_LldpLocSysName_Type())
lldpLocSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocSysName.setStatus(_A)
class _LldpLocSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocSysDesc_Type.__name__=_G
_LldpLocSysDesc_Object=MibScalar
lldpLocSysDesc=_LldpLocSysDesc_Object((1,3,6,1,4,1,52642,127,1,3,4),_LldpLocSysDesc_Type())
lldpLocSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocSysDesc.setStatus(_A)
_LldpLocSysCapSupported_Type=LldpSystemCapabilitiesMap
_LldpLocSysCapSupported_Object=MibScalar
lldpLocSysCapSupported=_LldpLocSysCapSupported_Object((1,3,6,1,4,1,52642,127,1,3,5),_LldpLocSysCapSupported_Type())
lldpLocSysCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocSysCapSupported.setStatus(_A)
_LldpLocSysCapEnabled_Type=LldpSystemCapabilitiesMap
_LldpLocSysCapEnabled_Object=MibScalar
lldpLocSysCapEnabled=_LldpLocSysCapEnabled_Object((1,3,6,1,4,1,52642,127,1,3,6),_LldpLocSysCapEnabled_Type())
lldpLocSysCapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocSysCapEnabled.setStatus(_A)
_LldpLocPortTable_Object=MibTable
lldpLocPortTable=_LldpLocPortTable_Object((1,3,6,1,4,1,52642,127,1,3,7))
if mibBuilder.loadTexts:lldpLocPortTable.setStatus(_A)
_LldpLocPortEntry_Object=MibTableRow
lldpLocPortEntry=_LldpLocPortEntry_Object((1,3,6,1,4,1,52642,127,1,3,7,1))
lldpLocPortEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:lldpLocPortEntry.setStatus(_A)
_LldpLocPortNum_Type=LldpPortNumber
_LldpLocPortNum_Object=MibTableColumn
lldpLocPortNum=_LldpLocPortNum_Object((1,3,6,1,4,1,52642,127,1,3,7,1,1),_LldpLocPortNum_Type())
lldpLocPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpLocPortNum.setStatus(_A)
_LldpLocPortIdSubtype_Type=LldpPortIdSubtype
_LldpLocPortIdSubtype_Object=MibTableColumn
lldpLocPortIdSubtype=_LldpLocPortIdSubtype_Object((1,3,6,1,4,1,52642,127,1,3,7,1,2),_LldpLocPortIdSubtype_Type())
lldpLocPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocPortIdSubtype.setStatus(_A)
_LldpLocPortId_Type=LldpPortId
_LldpLocPortId_Object=MibTableColumn
lldpLocPortId=_LldpLocPortId_Object((1,3,6,1,4,1,52642,127,1,3,7,1,3),_LldpLocPortId_Type())
lldpLocPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocPortId.setStatus(_A)
class _LldpLocPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocPortDesc_Type.__name__=_G
_LldpLocPortDesc_Object=MibTableColumn
lldpLocPortDesc=_LldpLocPortDesc_Object((1,3,6,1,4,1,52642,127,1,3,7,1,4),_LldpLocPortDesc_Type())
lldpLocPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocPortDesc.setStatus(_A)
_LldpLocManAddrTable_Object=MibTable
lldpLocManAddrTable=_LldpLocManAddrTable_Object((1,3,6,1,4,1,52642,127,1,3,8))
if mibBuilder.loadTexts:lldpLocManAddrTable.setStatus(_A)
_LldpLocManAddrEntry_Object=MibTableRow
lldpLocManAddrEntry=_LldpLocManAddrEntry_Object((1,3,6,1,4,1,52642,127,1,3,8,1))
lldpLocManAddrEntry.setIndexNames((0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:lldpLocManAddrEntry.setStatus(_A)
_LldpLocManAddrSubtype_Type=AddressFamilyNumbers
_LldpLocManAddrSubtype_Object=MibTableColumn
lldpLocManAddrSubtype=_LldpLocManAddrSubtype_Object((1,3,6,1,4,1,52642,127,1,3,8,1,1),_LldpLocManAddrSubtype_Type())
lldpLocManAddrSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpLocManAddrSubtype.setStatus(_A)
_LldpLocManAddr_Type=LldpManAddress
_LldpLocManAddr_Object=MibTableColumn
lldpLocManAddr=_LldpLocManAddr_Object((1,3,6,1,4,1,52642,127,1,3,8,1,2),_LldpLocManAddr_Type())
lldpLocManAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpLocManAddr.setStatus(_A)
_LldpLocManAddrLen_Type=Integer32
_LldpLocManAddrLen_Object=MibTableColumn
lldpLocManAddrLen=_LldpLocManAddrLen_Object((1,3,6,1,4,1,52642,127,1,3,8,1,3),_LldpLocManAddrLen_Type())
lldpLocManAddrLen.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocManAddrLen.setStatus(_A)
_LldpLocManAddrIfSubtype_Type=LldpManAddrIfSubtype
_LldpLocManAddrIfSubtype_Object=MibTableColumn
lldpLocManAddrIfSubtype=_LldpLocManAddrIfSubtype_Object((1,3,6,1,4,1,52642,127,1,3,8,1,4),_LldpLocManAddrIfSubtype_Type())
lldpLocManAddrIfSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocManAddrIfSubtype.setStatus(_A)
_LldpLocManAddrIfId_Type=Integer32
_LldpLocManAddrIfId_Object=MibTableColumn
lldpLocManAddrIfId=_LldpLocManAddrIfId_Object((1,3,6,1,4,1,52642,127,1,3,8,1,5),_LldpLocManAddrIfId_Type())
lldpLocManAddrIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocManAddrIfId.setStatus(_A)
_LldpLocManAddrOID_Type=ObjectIdentifier
_LldpLocManAddrOID_Object=MibTableColumn
lldpLocManAddrOID=_LldpLocManAddrOID_Object((1,3,6,1,4,1,52642,127,1,3,8,1,6),_LldpLocManAddrOID_Type())
lldpLocManAddrOID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpLocManAddrOID.setStatus(_A)
_LldpRemoteSystemsData_ObjectIdentity=ObjectIdentity
lldpRemoteSystemsData=_LldpRemoteSystemsData_ObjectIdentity((1,3,6,1,4,1,52642,127,1,4))
_LldpExtens_ObjectIdentity=ObjectIdentity
lldpExtens=_LldpExtens_ObjectIdentity((1,3,6,1,4,1,52642,127,1,4))
_LldpRemTable_Object=MibTable
lldpRemTable=_LldpRemTable_Object((1,3,6,1,4,1,52642,127,1,4,1))
if mibBuilder.loadTexts:lldpRemTable.setStatus(_A)
_LldpRemEntry_Object=MibTableRow
lldpRemEntry=_LldpRemEntry_Object((1,3,6,1,4,1,52642,127,1,4,1,1))
lldpRemEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:lldpRemEntry.setStatus(_A)
_LldpRemTimeMark_Type=TimeFilter
_LldpRemTimeMark_Object=MibTableColumn
lldpRemTimeMark=_LldpRemTimeMark_Object((1,3,6,1,4,1,52642,127,1,4,1,1,1),_LldpRemTimeMark_Type())
lldpRemTimeMark.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemTimeMark.setStatus(_A)
_LldpRemLocalPortNum_Type=LldpPortNumber
_LldpRemLocalPortNum_Object=MibTableColumn
lldpRemLocalPortNum=_LldpRemLocalPortNum_Object((1,3,6,1,4,1,52642,127,1,4,1,1,2),_LldpRemLocalPortNum_Type())
lldpRemLocalPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemLocalPortNum.setStatus(_A)
class _LldpRemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpRemIndex_Type.__name__=_E
_LldpRemIndex_Object=MibTableColumn
lldpRemIndex=_LldpRemIndex_Object((1,3,6,1,4,1,52642,127,1,4,1,1,3),_LldpRemIndex_Type())
lldpRemIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemIndex.setStatus(_A)
_LldpRemChassisIdSubtype_Type=LldpChassisIdSubtype
_LldpRemChassisIdSubtype_Object=MibTableColumn
lldpRemChassisIdSubtype=_LldpRemChassisIdSubtype_Object((1,3,6,1,4,1,52642,127,1,4,1,1,4),_LldpRemChassisIdSubtype_Type())
lldpRemChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemChassisIdSubtype.setStatus(_A)
_LldpRemChassisId_Type=LldpChassisId
_LldpRemChassisId_Object=MibTableColumn
lldpRemChassisId=_LldpRemChassisId_Object((1,3,6,1,4,1,52642,127,1,4,1,1,5),_LldpRemChassisId_Type())
lldpRemChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemChassisId.setStatus(_A)
_LldpRemPortIdSubtype_Type=LldpPortIdSubtype
_LldpRemPortIdSubtype_Object=MibTableColumn
lldpRemPortIdSubtype=_LldpRemPortIdSubtype_Object((1,3,6,1,4,1,52642,127,1,4,1,1,6),_LldpRemPortIdSubtype_Type())
lldpRemPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemPortIdSubtype.setStatus(_A)
_LldpRemPortId_Type=LldpPortId
_LldpRemPortId_Object=MibTableColumn
lldpRemPortId=_LldpRemPortId_Object((1,3,6,1,4,1,52642,127,1,4,1,1,7),_LldpRemPortId_Type())
lldpRemPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemPortId.setStatus(_A)
class _LldpRemPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpRemPortDesc_Type.__name__=_G
_LldpRemPortDesc_Object=MibTableColumn
lldpRemPortDesc=_LldpRemPortDesc_Object((1,3,6,1,4,1,52642,127,1,4,1,1,8),_LldpRemPortDesc_Type())
lldpRemPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemPortDesc.setStatus(_A)
class _LldpRemSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpRemSysName_Type.__name__=_G
_LldpRemSysName_Object=MibTableColumn
lldpRemSysName=_LldpRemSysName_Object((1,3,6,1,4,1,52642,127,1,4,1,1,9),_LldpRemSysName_Type())
lldpRemSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemSysName.setStatus(_A)
class _LldpRemSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpRemSysDesc_Type.__name__=_G
_LldpRemSysDesc_Object=MibTableColumn
lldpRemSysDesc=_LldpRemSysDesc_Object((1,3,6,1,4,1,52642,127,1,4,1,1,10),_LldpRemSysDesc_Type())
lldpRemSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemSysDesc.setStatus(_A)
_LldpRemSysCapSupported_Type=LldpSystemCapabilitiesMap
_LldpRemSysCapSupported_Object=MibTableColumn
lldpRemSysCapSupported=_LldpRemSysCapSupported_Object((1,3,6,1,4,1,52642,127,1,4,1,1,11),_LldpRemSysCapSupported_Type())
lldpRemSysCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemSysCapSupported.setStatus(_A)
_LldpRemSysCapEnabled_Type=LldpSystemCapabilitiesMap
_LldpRemSysCapEnabled_Object=MibTableColumn
lldpRemSysCapEnabled=_LldpRemSysCapEnabled_Object((1,3,6,1,4,1,52642,127,1,4,1,1,12),_LldpRemSysCapEnabled_Type())
lldpRemSysCapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemSysCapEnabled.setStatus(_A)
_LldpRemManAddrTable_Object=MibTable
lldpRemManAddrTable=_LldpRemManAddrTable_Object((1,3,6,1,4,1,52642,127,1,4,2))
if mibBuilder.loadTexts:lldpRemManAddrTable.setStatus(_A)
_LldpRemManAddrEntry_Object=MibTableRow
lldpRemManAddrEntry=_LldpRemManAddrEntry_Object((1,3,6,1,4,1,52642,127,1,4,2,1))
lldpRemManAddrEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:lldpRemManAddrEntry.setStatus(_A)
_LldpRemManAddrSubtype_Type=AddressFamilyNumbers
_LldpRemManAddrSubtype_Object=MibTableColumn
lldpRemManAddrSubtype=_LldpRemManAddrSubtype_Object((1,3,6,1,4,1,52642,127,1,4,2,1,1),_LldpRemManAddrSubtype_Type())
lldpRemManAddrSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemManAddrSubtype.setStatus(_A)
_LldpRemManAddr_Type=LldpManAddress
_LldpRemManAddr_Object=MibTableColumn
lldpRemManAddr=_LldpRemManAddr_Object((1,3,6,1,4,1,52642,127,1,4,2,1,2),_LldpRemManAddr_Type())
lldpRemManAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemManAddr.setStatus(_A)
_LldpRemManAddrIfSubtype_Type=LldpManAddrIfSubtype
_LldpRemManAddrIfSubtype_Object=MibTableColumn
lldpRemManAddrIfSubtype=_LldpRemManAddrIfSubtype_Object((1,3,6,1,4,1,52642,127,1,4,2,1,3),_LldpRemManAddrIfSubtype_Type())
lldpRemManAddrIfSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemManAddrIfSubtype.setStatus(_A)
_LldpRemManAddrIfId_Type=Integer32
_LldpRemManAddrIfId_Object=MibTableColumn
lldpRemManAddrIfId=_LldpRemManAddrIfId_Object((1,3,6,1,4,1,52642,127,1,4,2,1,4),_LldpRemManAddrIfId_Type())
lldpRemManAddrIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemManAddrIfId.setStatus(_A)
_LldpRemManAddrOID_Type=ObjectIdentifier
_LldpRemManAddrOID_Object=MibTableColumn
lldpRemManAddrOID=_LldpRemManAddrOID_Object((1,3,6,1,4,1,52642,127,1,4,2,1,5),_LldpRemManAddrOID_Type())
lldpRemManAddrOID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemManAddrOID.setStatus(_A)
_LldpRemUnknownTLVTable_Object=MibTable
lldpRemUnknownTLVTable=_LldpRemUnknownTLVTable_Object((1,3,6,1,4,1,52642,127,1,4,3))
if mibBuilder.loadTexts:lldpRemUnknownTLVTable.setStatus(_A)
_LldpRemUnknownTLVEntry_Object=MibTableRow
lldpRemUnknownTLVEntry=_LldpRemUnknownTLVEntry_Object((1,3,6,1,4,1,52642,127,1,4,3,1))
lldpRemUnknownTLVEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_g))
if mibBuilder.loadTexts:lldpRemUnknownTLVEntry.setStatus(_A)
class _LldpRemUnknownTLVType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9,126))
_LldpRemUnknownTLVType_Type.__name__=_E
_LldpRemUnknownTLVType_Object=MibTableColumn
lldpRemUnknownTLVType=_LldpRemUnknownTLVType_Object((1,3,6,1,4,1,52642,127,1,4,3,1,1),_LldpRemUnknownTLVType_Type())
lldpRemUnknownTLVType.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemUnknownTLVType.setStatus(_A)
class _LldpRemUnknownTLVInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_LldpRemUnknownTLVInfo_Type.__name__=_K
_LldpRemUnknownTLVInfo_Object=MibTableColumn
lldpRemUnknownTLVInfo=_LldpRemUnknownTLVInfo_Object((1,3,6,1,4,1,52642,127,1,4,3,1,2),_LldpRemUnknownTLVInfo_Type())
lldpRemUnknownTLVInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemUnknownTLVInfo.setStatus(_A)
_LldpRemOrgDefInfoTable_Object=MibTable
lldpRemOrgDefInfoTable=_LldpRemOrgDefInfoTable_Object((1,3,6,1,4,1,52642,127,1,4,4))
if mibBuilder.loadTexts:lldpRemOrgDefInfoTable.setStatus(_A)
_LldpRemOrgDefInfoEntry_Object=MibTableRow
lldpRemOrgDefInfoEntry=_LldpRemOrgDefInfoEntry_Object((1,3,6,1,4,1,52642,127,1,4,4,1))
lldpRemOrgDefInfoEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_h),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:lldpRemOrgDefInfoEntry.setStatus(_A)
class _LldpRemOrgDefInfoOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_LldpRemOrgDefInfoOUI_Type.__name__=_K
_LldpRemOrgDefInfoOUI_Object=MibTableColumn
lldpRemOrgDefInfoOUI=_LldpRemOrgDefInfoOUI_Object((1,3,6,1,4,1,52642,127,1,4,4,1,1),_LldpRemOrgDefInfoOUI_Type())
lldpRemOrgDefInfoOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemOrgDefInfoOUI.setStatus(_A)
class _LldpRemOrgDefInfoSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LldpRemOrgDefInfoSubtype_Type.__name__=_E
_LldpRemOrgDefInfoSubtype_Object=MibTableColumn
lldpRemOrgDefInfoSubtype=_LldpRemOrgDefInfoSubtype_Object((1,3,6,1,4,1,52642,127,1,4,4,1,2),_LldpRemOrgDefInfoSubtype_Type())
lldpRemOrgDefInfoSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemOrgDefInfoSubtype.setStatus(_A)
class _LldpRemOrgDefInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpRemOrgDefInfoIndex_Type.__name__=_E
_LldpRemOrgDefInfoIndex_Object=MibTableColumn
lldpRemOrgDefInfoIndex=_LldpRemOrgDefInfoIndex_Object((1,3,6,1,4,1,52642,127,1,4,4,1,3),_LldpRemOrgDefInfoIndex_Type())
lldpRemOrgDefInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRemOrgDefInfoIndex.setStatus(_A)
class _LldpRemOrgDefInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,507))
_LldpRemOrgDefInfo_Type.__name__=_K
_LldpRemOrgDefInfo_Object=MibTableColumn
lldpRemOrgDefInfo=_LldpRemOrgDefInfo_Object((1,3,6,1,4,1,52642,127,1,4,4,1,4),_LldpRemOrgDefInfo_Type())
lldpRemOrgDefInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemOrgDefInfo.setStatus(_A)
_LldpExtensions_ObjectIdentity=ObjectIdentity
lldpExtensions=_LldpExtensions_ObjectIdentity((1,3,6,1,4,1,52642,127,1,5))
_LldpConformance_ObjectIdentity=ObjectIdentity
lldpConformance=_LldpConformance_ObjectIdentity((1,3,6,1,4,1,52642,127,2))
_LldpCompliances_ObjectIdentity=ObjectIdentity
lldpCompliances=_LldpCompliances_ObjectIdentity((1,3,6,1,4,1,52642,127,2,1))
_LldpGroups_ObjectIdentity=ObjectIdentity
lldpGroups=_LldpGroups_ObjectIdentity((1,3,6,1,4,1,52642,127,2,2))
lldpLocManAddrEntry.registerAugmentions((_B,_k))
lldpConfigManAddrEntry.setIndexNames(*lldpLocManAddrEntry.getIndexNames())
lldpConfigGroup=ObjectGroup((1,3,6,1,4,1,52642,127,2,2,1))
lldpConfigGroup.setObjects((_B,_l))
if mibBuilder.loadTexts:lldpConfigGroup.setStatus(_A)
lldpConfigRxGroup=ObjectGroup((1,3,6,1,4,1,52642,127,2,2,2))
lldpConfigRxGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:lldpConfigRxGroup.setStatus(_A)
lldpConfigTxGroup=ObjectGroup((1,3,6,1,4,1,52642,127,2,2,3))
lldpConfigTxGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:lldpConfigTxGroup.setStatus(_A)
lldpStatsRxGroup=ObjectGroup((1,3,6,1,4,1,52642,127,2,2,4))
lldpStatsRxGroup.setObjects(*((_B,_u),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:lldpStatsRxGroup.setStatus(_A)
lldpStatsTxGroup=ObjectGroup((1,3,6,1,4,1,52642,127,2,2,5))
lldpStatsTxGroup.setObjects((_B,_A1))
if mibBuilder.loadTexts:lldpStatsTxGroup.setStatus(_A)
lldpLocSysGroup=ObjectGroup((1,3,6,1,4,1,52642,127,2,2,6))
lldpLocSysGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:lldpLocSysGroup.setStatus(_A)
lldpRemSysGroup=ObjectGroup((1,3,6,1,4,1,52642,127,2,2,7))
lldpRemSysGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:lldpRemSysGroup.setStatus(_A)
lldpRemTablesChange=NotificationType((1,3,6,1,4,1,52642,127,0,0,1))
lldpRemTablesChange.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:lldpRemTablesChange.setStatus(_A)
lldpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,52642,127,2,2,8))
lldpNotificationsGroup.setObjects((_B,_AT))
if mibBuilder.loadTexts:lldpNotificationsGroup.setStatus(_A)
lldpCompliance=ModuleCompliance((1,3,6,1,4,1,52642,127,2,1,1))
lldpCompliance.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:lldpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TimeFilter':TimeFilter,'ZeroBasedCounter32':ZeroBasedCounter32,'LldpChassisIdSubtype':LldpChassisIdSubtype,'LldpChassisId':LldpChassisId,'LldpPortIdSubtype':LldpPortIdSubtype,'LldpPortId':LldpPortId,'LldpManAddrIfSubtype':LldpManAddrIfSubtype,'LldpManAddress':LldpManAddress,'LldpSystemCapabilitiesMap':LldpSystemCapabilitiesMap,'LldpPortNumber':LldpPortNumber,_Y:LldpPortList,'nmslldpMIB':nmslldpMIB,'lldpNotifications':lldpNotifications,'lldpNotificationPrefix':lldpNotificationPrefix,_AT:lldpRemTablesChange,'lldpObjects':lldpObjects,'lldpConfiguration':lldpConfiguration,_o:lldpMessageTxInterval,_p:lldpMessageTxHoldMultiplier,_q:lldpReinitDelay,_r:lldpTxDelay,_m:lldpNotificationInterval,'lldpPortConfigTable':lldpPortConfigTable,'lldpPortConfigEntry':lldpPortConfigEntry,_X:lldpPortConfigPortNum,_l:lldpPortConfigAdminStatus,_n:lldpPortConfigNotificationEnable,_s:lldpPortConfigTLVsTxEnable,'lldpConfigManAddrTable':lldpConfigManAddrTable,_k:lldpConfigManAddrEntry,_t:lldpConfigManAddrPortsTxEnable,'lldpStatistics':lldpStatistics,_u:lldpStatsRemTablesLastChangeTime,_N:lldpStatsRemTablesInserts,_O:lldpStatsRemTablesDeletes,_P:lldpStatsRemTablesDrops,_Q:lldpStatsRemTablesAgeouts,'lldpStatsTxPortTable':lldpStatsTxPortTable,'lldpStatsTxPortEntry':lldpStatsTxPortEntry,_Z:lldpStatsTxPortNum,_A1:lldpStatsTxPortFramesTotal,'lldpStatsRxPortTable':lldpStatsRxPortTable,'lldpStatsRxPortEntry':lldpStatsRxPortEntry,_a:lldpStatsRxPortNum,_v:lldpStatsRxPortFramesDiscardedTotal,_w:lldpStatsRxPortFramesErrors,_x:lldpStatsRxPortFramesTotal,_y:lldpStatsRxPortTLVsDiscardedTotal,_z:lldpStatsRxPortTLVsUnrecognizedTotal,_A0:lldpStatsRxPortAgeoutsTotal,'lldpLocalSystemData':lldpLocalSystemData,_A2:lldpLocChassisIdSubtype,_A3:lldpLocChassisId,_A8:lldpLocSysName,_A7:lldpLocSysDesc,_A9:lldpLocSysCapSupported,_AA:lldpLocSysCapEnabled,'lldpLocPortTable':lldpLocPortTable,'lldpLocPortEntry':lldpLocPortEntry,_b:lldpLocPortNum,_A4:lldpLocPortIdSubtype,_A5:lldpLocPortId,_A6:lldpLocPortDesc,'lldpLocManAddrTable':lldpLocManAddrTable,'lldpLocManAddrEntry':lldpLocManAddrEntry,_c:lldpLocManAddrSubtype,_d:lldpLocManAddr,_AB:lldpLocManAddrLen,_AC:lldpLocManAddrIfSubtype,_AD:lldpLocManAddrIfId,_AE:lldpLocManAddrOID,'lldpRemoteSystemsData':lldpRemoteSystemsData,'lldpExtens':lldpExtens,'lldpRemTable':lldpRemTable,'lldpRemEntry':lldpRemEntry,_H:lldpRemTimeMark,_I:lldpRemLocalPortNum,_J:lldpRemIndex,_AF:lldpRemChassisIdSubtype,_AG:lldpRemChassisId,_AH:lldpRemPortIdSubtype,_AI:lldpRemPortId,_AJ:lldpRemPortDesc,_AK:lldpRemSysName,_AL:lldpRemSysDesc,_AM:lldpRemSysCapSupported,_AN:lldpRemSysCapEnabled,'lldpRemManAddrTable':lldpRemManAddrTable,'lldpRemManAddrEntry':lldpRemManAddrEntry,_e:lldpRemManAddrSubtype,_f:lldpRemManAddr,_AO:lldpRemManAddrIfSubtype,_AP:lldpRemManAddrIfId,_AQ:lldpRemManAddrOID,'lldpRemUnknownTLVTable':lldpRemUnknownTLVTable,'lldpRemUnknownTLVEntry':lldpRemUnknownTLVEntry,_g:lldpRemUnknownTLVType,_AR:lldpRemUnknownTLVInfo,'lldpRemOrgDefInfoTable':lldpRemOrgDefInfoTable,'lldpRemOrgDefInfoEntry':lldpRemOrgDefInfoEntry,_h:lldpRemOrgDefInfoOUI,_i:lldpRemOrgDefInfoSubtype,_j:lldpRemOrgDefInfoIndex,_AS:lldpRemOrgDefInfo,'lldpExtensions':lldpExtensions,'lldpConformance':lldpConformance,'lldpCompliances':lldpCompliances,'lldpCompliance':lldpCompliance,'lldpGroups':lldpGroups,_AU:lldpConfigGroup,_AV:lldpConfigRxGroup,_AW:lldpConfigTxGroup,_AX:lldpStatsRxGroup,_AY:lldpStatsTxGroup,_AZ:lldpLocSysGroup,_Aa:lldpRemSysGroup,_Ab:lldpNotificationsGroup})