_Al='ciscoLS1010ChassisMIBGroup2'
_Ak='clsInletTempGroup'
_Aj='clsOperStatusGroup'
_Ai='clsPortLedGroup1'
_Ah='clsEnetPortGroup1'
_Ag='ciscoLS1010ChassisChangeNotification'
_Af='ciscoLS1010ChassisFailureNotification'
_Ae='ciscoLS1010SubModuleSerialNumberString'
_Ad='ciscoLS1010ModuleSerialNumberString'
_Ac='ciscoLS1010ModuleHwVersionMinor'
_Ab='clsPortLedStatus'
_Aa='clsPortLedType'
_AZ='clsEnetPortLinkStatus'
_AY='clsEnetPortType'
_AX='clsEnetPortAdminSpeed'
_AW='clsEnetPortDuplex'
_AV='ciscols1010SystemClockSourcePriority'
_AU='ciscols1010SystemClockSourceStatus'
_AT='ciscoLS1010ChassisClockingMode'
_AS='ciscoAtmCpuTerminateOamFlow'
_AR='clsPortLedIndex'
_AQ='ciscoAtmSwitchInvalidCellHeaderIndex'
_AP='ciscoLS1010PortIndex'
_AO='criticalWarning'
_AN='majorWarning'
_AM='minorWarning'
_AL='overTemperature'
_AK='cisco6400'
_AJ='Unsigned32'
_AI='OctetString'
_AH='ciscoLS1010ChassisMIBRev1Group'
_AG='ciscoAtmInterceptEndToEndOamFlow'
_AF='ciscoLS1010ModuleOperStatus'
_AE='ciscoLS1010ChassisInletTempStatus'
_AD='ciscoLS1010SubModuleIndex'
_AC='deprecated'
_AB='reset'
_AA='TruthValue'
_A9='ifIndex'
_A8='IF-MIB'
_A7='ciscoLS1010ChassisMIBGroup1'
_A6='ciscoLS1010ChassisMIBGroup'
_A5='ciscoLS1010SubModuleOperStatus'
_A4='ciscoLS1010SubModuleHwVersionMinor'
_A3='ciscoAtmSwitchInvalidCellHeader'
_A2='ciscoAtmSwitchInvalidCells'
_A1='ciscoAtmSwitchDiscardCells'
_A0='ciscoAtmSwitchFreeBuffer'
_z='ciscoAtmSwitchTotalBuffer'
_y='ciscoAtmCpuAdminStatus'
_x='ciscoLS1010PortIfIndex'
_w='ciscoLS1010SubModuleAdminStatus'
_v='ciscoLS1010SubModuleNumPorts'
_u='ciscoLS1010SubModuleDescr'
_t='ciscoLS1010SubModuleSwVersion'
_s='ciscoLS1010SubModuleHwVersion'
_r='ciscoLS1010SubModuleSerialNumber'
_q='ciscoLS1010SubModuleType'
_p='ciscoLS1010ModuleAdminStatus'
_o='ciscoLS1010ModuleNumSubModules'
_n='ciscoLS1010ModuleDescr'
_m='ciscoLS1010ModuleSwVersion'
_l='ciscoLS1010ModuleHwVersion'
_k='ciscoLS1010ModuleSerialNumber'
_j='ciscoLS1010ModuleType'
_i='ciscoLS1010ChassisChangeAction'
_h='ciscoLS1010ChassisFailureAction'
_g='ciscoLS1010ChassisLastChange'
_f='ciscoLS1010ChassisNumSlots'
_e='ciscoLS1010ChassisPcmciaSlot1Type'
_d='ciscoLS1010ChassisPcmciaSlot0Type'
_c='ciscoLS1010ChassisEnetLinkLed'
_b='ciscoLS1010ChassisCardStatusLed'
_a='ciscoLS1010ChassisFanLed'
_Z='ciscoLS1010ChassisPs1Led'
_Y='ciscoLS1010ChassisPs1AdminStatus'
_X='ciscoLS1010ChassisPs1Type'
_W='ciscoLS1010ChassisPs0Led'
_V='ciscoLS1010ChassisPs0AdminStatus'
_U='ciscoLS1010ChassisPs0Type'
_T='ciscoLS1010ChassisBkplType'
_S='ciscoLS1010ChassisSysType'
_R='ciscoLS1010ModuleIndex'
_Q='other'
_P='empty'
_O='ciscoLS1010ChassisTempStatus'
_N='ciscoLS1010Chassis12VoltStatus'
_M='ciscoLS1010ChassisFanStatus'
_L='ciscoLS1010ChassisPs1Status'
_K='ciscoLS1010ChassisPs0Status'
_J='not-accessible'
_I='ciscoLS1010ChassisMIBClockingGroup'
_H='ok'
_G='obsolete'
_F='unknown'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-RHINO-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_AI,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
workgroup,=mibBuilder.importSymbols('CISCO-SMI','workgroup')
Unsigned32,=mibBuilder.importSymbols('CISCO-TC',_AJ)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_A8,'InterfaceIndex',_A9)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_AJ,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_AA)
ciscoLS1010ChassisMIB=ModuleIdentity((1,3,6,1,4,1,9,5,11))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIB.setRevisions(('2001-03-29 00:00','2001-02-15 00:00','2000-07-20 00:00','2000-04-11 00:00','2000-02-07 00:00','1999-11-30 00:00','1999-10-04 00:00','1999-06-29 00:00','1999-06-17 00:00','1999-03-12 00:00','1998-12-02 00:00','1998-10-26 00:00','1998-07-13 00:00','1997-11-20 00:00','1997-07-22 00:00','1997-02-04 00:00','1996-10-02 00:00','1995-10-02 00:00'))
class PsType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('powerone',0),('astec',1),('minus48VDC',2),(_P,3),('ac1100W',4),('ac1200W',5),('dc1200W',6),('pem',7),('ac1360W',8),('dc1360W',9),('ac2000W',10),('dc2000W',11),('acpem',12),('ac175W',13)))
class OperStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_H,2),('fault',3),('fanAlarm',4),('partialFault',5),(_P,6)))
class AdminStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),(_AB,3)))
class Led(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('off',1),('green',2),('red',3),('yellow',4),('blinkgreen',5),('blinkyellow',6),('blinkred',7),(_F,8)))
class PcmciaType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_P,2),('flash',3),('disk',4)))
_CiscoLS1010ChassisMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLS1010ChassisMIBObjects=_CiscoLS1010ChassisMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,5,11,1))
_CiscoLS1010ChassisGroup_ObjectIdentity=ObjectIdentity
ciscoLS1010ChassisGroup=_CiscoLS1010ChassisGroup_ObjectIdentity((1,3,6,1,4,1,9,5,11,1,1))
class _CiscoLS1010ChassisSysType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_Q,1),('ls1010',2),('c8510',3),(_AK,4),('c8540',5),('tgx8750',6),('wsx6302',7),('c2948g',8),('c4908g',9)))
_CiscoLS1010ChassisSysType_Type.__name__=_D
_CiscoLS1010ChassisSysType_Object=MibScalar
ciscoLS1010ChassisSysType=_CiscoLS1010ChassisSysType_Object((1,3,6,1,4,1,9,5,11,1,1,1),_CiscoLS1010ChassisSysType_Type())
ciscoLS1010ChassisSysType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisSysType.setStatus(_B)
class _CiscoLS1010ChassisBkplType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Q,1),('atm',2),('c5500',3),(_AK,4),('c8510',5),('c8540',6),('tgx8750',7),('cat6000',8),('c2948g',9),('c4908g',10)))
_CiscoLS1010ChassisBkplType_Type.__name__=_D
_CiscoLS1010ChassisBkplType_Object=MibScalar
ciscoLS1010ChassisBkplType=_CiscoLS1010ChassisBkplType_Object((1,3,6,1,4,1,9,5,11,1,1,2),_CiscoLS1010ChassisBkplType_Type())
ciscoLS1010ChassisBkplType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisBkplType.setStatus(_B)
_CiscoLS1010ChassisPs0Type_Type=PsType
_CiscoLS1010ChassisPs0Type_Object=MibScalar
ciscoLS1010ChassisPs0Type=_CiscoLS1010ChassisPs0Type_Object((1,3,6,1,4,1,9,5,11,1,1,3),_CiscoLS1010ChassisPs0Type_Type())
ciscoLS1010ChassisPs0Type.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisPs0Type.setStatus(_B)
_CiscoLS1010ChassisPs0AdminStatus_Type=AdminStatus
_CiscoLS1010ChassisPs0AdminStatus_Object=MibScalar
ciscoLS1010ChassisPs0AdminStatus=_CiscoLS1010ChassisPs0AdminStatus_Object((1,3,6,1,4,1,9,5,11,1,1,4),_CiscoLS1010ChassisPs0AdminStatus_Type())
ciscoLS1010ChassisPs0AdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoLS1010ChassisPs0AdminStatus.setStatus(_B)
_CiscoLS1010ChassisPs0Status_Type=OperStatus
_CiscoLS1010ChassisPs0Status_Object=MibScalar
ciscoLS1010ChassisPs0Status=_CiscoLS1010ChassisPs0Status_Object((1,3,6,1,4,1,9,5,11,1,1,5),_CiscoLS1010ChassisPs0Status_Type())
ciscoLS1010ChassisPs0Status.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisPs0Status.setStatus(_B)
_CiscoLS1010ChassisPs0Led_Type=Led
_CiscoLS1010ChassisPs0Led_Object=MibScalar
ciscoLS1010ChassisPs0Led=_CiscoLS1010ChassisPs0Led_Object((1,3,6,1,4,1,9,5,11,1,1,6),_CiscoLS1010ChassisPs0Led_Type())
ciscoLS1010ChassisPs0Led.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisPs0Led.setStatus(_B)
_CiscoLS1010ChassisPs1Type_Type=PsType
_CiscoLS1010ChassisPs1Type_Object=MibScalar
ciscoLS1010ChassisPs1Type=_CiscoLS1010ChassisPs1Type_Object((1,3,6,1,4,1,9,5,11,1,1,7),_CiscoLS1010ChassisPs1Type_Type())
ciscoLS1010ChassisPs1Type.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisPs1Type.setStatus(_B)
_CiscoLS1010ChassisPs1AdminStatus_Type=AdminStatus
_CiscoLS1010ChassisPs1AdminStatus_Object=MibScalar
ciscoLS1010ChassisPs1AdminStatus=_CiscoLS1010ChassisPs1AdminStatus_Object((1,3,6,1,4,1,9,5,11,1,1,8),_CiscoLS1010ChassisPs1AdminStatus_Type())
ciscoLS1010ChassisPs1AdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoLS1010ChassisPs1AdminStatus.setStatus(_B)
_CiscoLS1010ChassisPs1Status_Type=OperStatus
_CiscoLS1010ChassisPs1Status_Object=MibScalar
ciscoLS1010ChassisPs1Status=_CiscoLS1010ChassisPs1Status_Object((1,3,6,1,4,1,9,5,11,1,1,9),_CiscoLS1010ChassisPs1Status_Type())
ciscoLS1010ChassisPs1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisPs1Status.setStatus(_B)
_CiscoLS1010ChassisPs1Led_Type=Led
_CiscoLS1010ChassisPs1Led_Object=MibScalar
ciscoLS1010ChassisPs1Led=_CiscoLS1010ChassisPs1Led_Object((1,3,6,1,4,1,9,5,11,1,1,10),_CiscoLS1010ChassisPs1Led_Type())
ciscoLS1010ChassisPs1Led.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisPs1Led.setStatus(_B)
_CiscoLS1010ChassisFanStatus_Type=OperStatus
_CiscoLS1010ChassisFanStatus_Object=MibScalar
ciscoLS1010ChassisFanStatus=_CiscoLS1010ChassisFanStatus_Object((1,3,6,1,4,1,9,5,11,1,1,11),_CiscoLS1010ChassisFanStatus_Type())
ciscoLS1010ChassisFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisFanStatus.setStatus(_B)
_CiscoLS1010ChassisFanLed_Type=Led
_CiscoLS1010ChassisFanLed_Object=MibScalar
ciscoLS1010ChassisFanLed=_CiscoLS1010ChassisFanLed_Object((1,3,6,1,4,1,9,5,11,1,1,12),_CiscoLS1010ChassisFanLed_Type())
ciscoLS1010ChassisFanLed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisFanLed.setStatus(_B)
_CiscoLS1010ChassisCardStatusLed_Type=Led
_CiscoLS1010ChassisCardStatusLed_Object=MibScalar
ciscoLS1010ChassisCardStatusLed=_CiscoLS1010ChassisCardStatusLed_Object((1,3,6,1,4,1,9,5,11,1,1,13),_CiscoLS1010ChassisCardStatusLed_Type())
ciscoLS1010ChassisCardStatusLed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisCardStatusLed.setStatus(_B)
_CiscoLS1010ChassisEnetLinkLed_Type=Led
_CiscoLS1010ChassisEnetLinkLed_Object=MibScalar
ciscoLS1010ChassisEnetLinkLed=_CiscoLS1010ChassisEnetLinkLed_Object((1,3,6,1,4,1,9,5,11,1,1,14),_CiscoLS1010ChassisEnetLinkLed_Type())
ciscoLS1010ChassisEnetLinkLed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisEnetLinkLed.setStatus(_B)
class _CiscoLS1010Chassis12VoltStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('outOfTolerance',2),(_F,3)))
_CiscoLS1010Chassis12VoltStatus_Type.__name__=_D
_CiscoLS1010Chassis12VoltStatus_Object=MibScalar
ciscoLS1010Chassis12VoltStatus=_CiscoLS1010Chassis12VoltStatus_Object((1,3,6,1,4,1,9,5,11,1,1,15),_CiscoLS1010Chassis12VoltStatus_Type())
ciscoLS1010Chassis12VoltStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010Chassis12VoltStatus.setStatus(_B)
class _CiscoLS1010ChassisTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_AL,2),(_AM,3),(_AN,4),(_AO,5)))
_CiscoLS1010ChassisTempStatus_Type.__name__=_D
_CiscoLS1010ChassisTempStatus_Object=MibScalar
ciscoLS1010ChassisTempStatus=_CiscoLS1010ChassisTempStatus_Object((1,3,6,1,4,1,9,5,11,1,1,16),_CiscoLS1010ChassisTempStatus_Type())
ciscoLS1010ChassisTempStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisTempStatus.setStatus(_B)
_CiscoLS1010ChassisPcmciaSlot0Type_Type=PcmciaType
_CiscoLS1010ChassisPcmciaSlot0Type_Object=MibScalar
ciscoLS1010ChassisPcmciaSlot0Type=_CiscoLS1010ChassisPcmciaSlot0Type_Object((1,3,6,1,4,1,9,5,11,1,1,17),_CiscoLS1010ChassisPcmciaSlot0Type_Type())
ciscoLS1010ChassisPcmciaSlot0Type.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisPcmciaSlot0Type.setStatus(_B)
_CiscoLS1010ChassisPcmciaSlot1Type_Type=PcmciaType
_CiscoLS1010ChassisPcmciaSlot1Type_Object=MibScalar
ciscoLS1010ChassisPcmciaSlot1Type=_CiscoLS1010ChassisPcmciaSlot1Type_Object((1,3,6,1,4,1,9,5,11,1,1,18),_CiscoLS1010ChassisPcmciaSlot1Type_Type())
ciscoLS1010ChassisPcmciaSlot1Type.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisPcmciaSlot1Type.setStatus(_B)
class _CiscoLS1010ChassisNumSlots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CiscoLS1010ChassisNumSlots_Type.__name__=_D
_CiscoLS1010ChassisNumSlots_Object=MibScalar
ciscoLS1010ChassisNumSlots=_CiscoLS1010ChassisNumSlots_Object((1,3,6,1,4,1,9,5,11,1,1,19),_CiscoLS1010ChassisNumSlots_Type())
ciscoLS1010ChassisNumSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisNumSlots.setStatus(_B)
_CiscoLS1010ChassisLastChange_Type=TimeStamp
_CiscoLS1010ChassisLastChange_Object=MibScalar
ciscoLS1010ChassisLastChange=_CiscoLS1010ChassisLastChange_Object((1,3,6,1,4,1,9,5,11,1,1,20),_CiscoLS1010ChassisLastChange_Type())
ciscoLS1010ChassisLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisLastChange.setStatus(_B)
class _CiscoLS1010ChassisFailureAction_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nothing',1),('sendTrap',2),('shutdown',3),('sendTrapAndShutdown',4)))
_CiscoLS1010ChassisFailureAction_Type.__name__=_D
_CiscoLS1010ChassisFailureAction_Object=MibScalar
ciscoLS1010ChassisFailureAction=_CiscoLS1010ChassisFailureAction_Object((1,3,6,1,4,1,9,5,11,1,1,21),_CiscoLS1010ChassisFailureAction_Type())
ciscoLS1010ChassisFailureAction.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoLS1010ChassisFailureAction.setStatus(_B)
class _CiscoLS1010ChassisChangeAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nothing',1),('sendTrap',2)))
_CiscoLS1010ChassisChangeAction_Type.__name__=_D
_CiscoLS1010ChassisChangeAction_Object=MibScalar
ciscoLS1010ChassisChangeAction=_CiscoLS1010ChassisChangeAction_Object((1,3,6,1,4,1,9,5,11,1,1,22),_CiscoLS1010ChassisChangeAction_Type())
ciscoLS1010ChassisChangeAction.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoLS1010ChassisChangeAction.setStatus(_B)
class _CiscoLS1010ChassisClockingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('revertive',1),('nonRevertive',2)))
_CiscoLS1010ChassisClockingMode_Type.__name__=_D
_CiscoLS1010ChassisClockingMode_Object=MibScalar
ciscoLS1010ChassisClockingMode=_CiscoLS1010ChassisClockingMode_Object((1,3,6,1,4,1,9,5,11,1,1,23),_CiscoLS1010ChassisClockingMode_Type())
ciscoLS1010ChassisClockingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoLS1010ChassisClockingMode.setStatus(_B)
class _Ciscols1010SystemClockSourceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSelected',1),('selected',2)))
_Ciscols1010SystemClockSourceStatus_Type.__name__=_D
_Ciscols1010SystemClockSourceStatus_Object=MibScalar
ciscols1010SystemClockSourceStatus=_Ciscols1010SystemClockSourceStatus_Object((1,3,6,1,4,1,9,5,11,1,1,24),_Ciscols1010SystemClockSourceStatus_Type())
ciscols1010SystemClockSourceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscols1010SystemClockSourceStatus.setStatus(_B)
class _Ciscols1010SystemClockSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('priority1',1),('priority2',2),('priority3',3),('priority4',4),('priority5',5)))
_Ciscols1010SystemClockSourcePriority_Type.__name__=_D
_Ciscols1010SystemClockSourcePriority_Object=MibScalar
ciscols1010SystemClockSourcePriority=_Ciscols1010SystemClockSourcePriority_Object((1,3,6,1,4,1,9,5,11,1,1,25),_Ciscols1010SystemClockSourcePriority_Type())
ciscols1010SystemClockSourcePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscols1010SystemClockSourcePriority.setStatus(_B)
class _CiscoLS1010ChassisInletTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_AL,2),(_AM,3),(_AN,4),(_AO,5),(_F,6)))
_CiscoLS1010ChassisInletTempStatus_Type.__name__=_D
_CiscoLS1010ChassisInletTempStatus_Object=MibScalar
ciscoLS1010ChassisInletTempStatus=_CiscoLS1010ChassisInletTempStatus_Object((1,3,6,1,4,1,9,5,11,1,1,26),_CiscoLS1010ChassisInletTempStatus_Type())
ciscoLS1010ChassisInletTempStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ChassisInletTempStatus.setStatus(_B)
_CiscoLS1010ModuleGroup_ObjectIdentity=ObjectIdentity
ciscoLS1010ModuleGroup=_CiscoLS1010ModuleGroup_ObjectIdentity((1,3,6,1,4,1,9,5,11,1,2))
_CiscoLS1010ModuleTable_Object=MibTable
ciscoLS1010ModuleTable=_CiscoLS1010ModuleTable_Object((1,3,6,1,4,1,9,5,11,1,2,1))
if mibBuilder.loadTexts:ciscoLS1010ModuleTable.setStatus(_B)
_CiscoLS1010ModuleEntry_Object=MibTableRow
ciscoLS1010ModuleEntry=_CiscoLS1010ModuleEntry_Object((1,3,6,1,4,1,9,5,11,1,2,1,1))
ciscoLS1010ModuleEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:ciscoLS1010ModuleEntry.setStatus(_B)
class _CiscoLS1010ModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CiscoLS1010ModuleIndex_Type.__name__=_D
_CiscoLS1010ModuleIndex_Object=MibTableColumn
ciscoLS1010ModuleIndex=_CiscoLS1010ModuleIndex_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,1),_CiscoLS1010ModuleIndex_Type())
ciscoLS1010ModuleIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoLS1010ModuleIndex.setStatus(_B)
class _CiscoLS1010ModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_Q,1),('carrier',2),('cpuSwitchAndFeature',3),('cpuSwitchAndFeaturePFQ',4),('superCarrier',5),('cpuRoute',6),('switch10GAndFC',7),('switch10GNoFC',8),('atmFabricIntegration',9),('dualSlot',10),('cmpmCarrier',11),('tsCarrier',12),('nodeSwitchProcessor2ndGeneration',13)))
_CiscoLS1010ModuleType_Type.__name__=_D
_CiscoLS1010ModuleType_Object=MibTableColumn
ciscoLS1010ModuleType=_CiscoLS1010ModuleType_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,2),_CiscoLS1010ModuleType_Type())
ciscoLS1010ModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleType.setStatus(_B)
_CiscoLS1010ModuleSerialNumber_Type=Integer32
_CiscoLS1010ModuleSerialNumber_Object=MibTableColumn
ciscoLS1010ModuleSerialNumber=_CiscoLS1010ModuleSerialNumber_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,3),_CiscoLS1010ModuleSerialNumber_Type())
ciscoLS1010ModuleSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleSerialNumber.setStatus(_AC)
_CiscoLS1010ModuleHwVersion_Type=Integer32
_CiscoLS1010ModuleHwVersion_Object=MibTableColumn
ciscoLS1010ModuleHwVersion=_CiscoLS1010ModuleHwVersion_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,4),_CiscoLS1010ModuleHwVersion_Type())
ciscoLS1010ModuleHwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleHwVersion.setStatus(_B)
_CiscoLS1010ModuleSwVersion_Type=Integer32
_CiscoLS1010ModuleSwVersion_Object=MibTableColumn
ciscoLS1010ModuleSwVersion=_CiscoLS1010ModuleSwVersion_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,5),_CiscoLS1010ModuleSwVersion_Type())
ciscoLS1010ModuleSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleSwVersion.setStatus(_B)
_CiscoLS1010ModuleDescr_Type=DisplayString
_CiscoLS1010ModuleDescr_Object=MibTableColumn
ciscoLS1010ModuleDescr=_CiscoLS1010ModuleDescr_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,6),_CiscoLS1010ModuleDescr_Type())
ciscoLS1010ModuleDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleDescr.setStatus(_B)
class _CiscoLS1010ModuleNumSubModules_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoLS1010ModuleNumSubModules_Type.__name__=_D
_CiscoLS1010ModuleNumSubModules_Object=MibTableColumn
ciscoLS1010ModuleNumSubModules=_CiscoLS1010ModuleNumSubModules_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,7),_CiscoLS1010ModuleNumSubModules_Type())
ciscoLS1010ModuleNumSubModules.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleNumSubModules.setStatus(_B)
_CiscoLS1010ModuleAdminStatus_Type=AdminStatus
_CiscoLS1010ModuleAdminStatus_Object=MibTableColumn
ciscoLS1010ModuleAdminStatus=_CiscoLS1010ModuleAdminStatus_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,8),_CiscoLS1010ModuleAdminStatus_Type())
ciscoLS1010ModuleAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoLS1010ModuleAdminStatus.setStatus(_B)
_CiscoLS1010ModuleOperStatus_Type=OperStatus
_CiscoLS1010ModuleOperStatus_Object=MibTableColumn
ciscoLS1010ModuleOperStatus=_CiscoLS1010ModuleOperStatus_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,9),_CiscoLS1010ModuleOperStatus_Type())
ciscoLS1010ModuleOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleOperStatus.setStatus(_B)
_CiscoLS1010ModuleHwVersionMinor_Type=Unsigned32
_CiscoLS1010ModuleHwVersionMinor_Object=MibTableColumn
ciscoLS1010ModuleHwVersionMinor=_CiscoLS1010ModuleHwVersionMinor_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,10),_CiscoLS1010ModuleHwVersionMinor_Type())
ciscoLS1010ModuleHwVersionMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleHwVersionMinor.setStatus(_B)
_CiscoLS1010ModuleSerialNumberString_Type=DisplayString
_CiscoLS1010ModuleSerialNumberString_Object=MibTableColumn
ciscoLS1010ModuleSerialNumberString=_CiscoLS1010ModuleSerialNumberString_Object((1,3,6,1,4,1,9,5,11,1,2,1,1,11),_CiscoLS1010ModuleSerialNumberString_Type())
ciscoLS1010ModuleSerialNumberString.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010ModuleSerialNumberString.setStatus(_B)
_CiscoLS1010SubModuleGroup_ObjectIdentity=ObjectIdentity
ciscoLS1010SubModuleGroup=_CiscoLS1010SubModuleGroup_ObjectIdentity((1,3,6,1,4,1,9,5,11,1,3))
_CiscoLS1010SubModuleTable_Object=MibTable
ciscoLS1010SubModuleTable=_CiscoLS1010SubModuleTable_Object((1,3,6,1,4,1,9,5,11,1,3,1))
if mibBuilder.loadTexts:ciscoLS1010SubModuleTable.setStatus(_B)
_CiscoLS1010SubModuleEntry_Object=MibTableRow
ciscoLS1010SubModuleEntry=_CiscoLS1010SubModuleEntry_Object((1,3,6,1,4,1,9,5,11,1,3,1,1))
ciscoLS1010SubModuleEntry.setIndexNames((0,_A,_R),(0,_A,_AD))
if mibBuilder.loadTexts:ciscoLS1010SubModuleEntry.setStatus(_B)
class _CiscoLS1010SubModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CiscoLS1010SubModuleIndex_Type.__name__=_D
_CiscoLS1010SubModuleIndex_Object=MibTableColumn
ciscoLS1010SubModuleIndex=_CiscoLS1010SubModuleIndex_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,1),_CiscoLS1010SubModuleIndex_Type())
ciscoLS1010SubModuleIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoLS1010SubModuleIndex.setStatus(_B)
class _CiscoLS1010SubModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98)));namedValues=NamedValues(*((_Q,1),('oc3Utp5',2),('oc3SingleModeFiber',3),('oc3MultiModeFiber',4),('oc12SingleModeFiber',5),('oc12MultiModeFiber',6),('ds3',7),('e3',8),('cpuSwitch',9),('featureFpga',10),('featureAsic',11),('t1',12),('e1',13),('e1bnc',14),('oc3Mixed',15),('cbrt1',16),('cbr120e1',17),('cbr75e1',18),('quadDs3',19),('quadE3',20),('dualDs3',21),('dualE3',22),('oc12Mixed',23),('atm25',24),('featurePVC',25),('routerProcessorAlpha',26),('dualOC3SingleModeIRFiber',27),('dualOC3MultiModeIRFiber',28),('routerProcessorBeta',29),('fratm1CT3',30),('fratm4CE1',31),('oc3SingleModeLRFiber',35),('oc12SingleModeLRFiber',36),('sixPortDS3',37),('feUTP8p16k',40),('feUTP8p64k',41),('feMMF8p16k',42),('feMMF8p64k',43),('feUTP16p16k',44),('feUTP16p64k',45),('feMMF16p16k',46),('feMMF16p64k',47),('geF1p16k',48),('geF1p64k',49),('geF2p16k',50),('geF2p64k',51),('feBridge4p',52),('feUTP8p16kFullDup',53),('feUTP8p64kFullDup',54),('routeProc',55),('switch10GProc',56),('featureNetClock',57),('featureABR',58),('geF8p64k',59),('featureLite',60),('s16pOC3MM',61),('s16pOC3SM',62),('s4pOC12MM',63),('s4pOC12SM',64),('atmIma8pT1',65),('atmIma8pE1',66),('atm25m4p',67),('s1pOC48cSM',68),('s1pOC48cSMLR',69),('atmFIMBridge',70),('atmFIMoc12MM',71),('arm1p64k',80),('arm2p64k',81),('xpif1pGE16k',82),('xpif1pGE64k',83),('xpif1pGE256k',84),('xpifAtm1pOC12SMIR64k',85),('xpifAtm1pOC12SMIR256k',86),('xpifAtm1pOC12MM64k',87),('xpifAtm1pOC12MM256k',88),('xpifAtm1pOC3SMIR64k',89),('xpifAtm1pOC3SMIR256k',90),('xpifAtm1pOC3MM64k',91),('xpifAtm1pOC3MM256k',92),('xpifPos1pOC12SMIR64k',93),('xpifPos1pOC12SMIR256k',94),('xpifPos1pOC12SMLR64k',95),('xpifPos1pOC12SMLR256k',96),('xpifArm2p256k',97),('aclDaughter',98)))
_CiscoLS1010SubModuleType_Type.__name__=_D
_CiscoLS1010SubModuleType_Object=MibTableColumn
ciscoLS1010SubModuleType=_CiscoLS1010SubModuleType_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,2),_CiscoLS1010SubModuleType_Type())
ciscoLS1010SubModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleType.setStatus(_B)
_CiscoLS1010SubModuleSerialNumber_Type=Integer32
_CiscoLS1010SubModuleSerialNumber_Object=MibTableColumn
ciscoLS1010SubModuleSerialNumber=_CiscoLS1010SubModuleSerialNumber_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,3),_CiscoLS1010SubModuleSerialNumber_Type())
ciscoLS1010SubModuleSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleSerialNumber.setStatus(_AC)
_CiscoLS1010SubModuleHwVersion_Type=Integer32
_CiscoLS1010SubModuleHwVersion_Object=MibTableColumn
ciscoLS1010SubModuleHwVersion=_CiscoLS1010SubModuleHwVersion_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,4),_CiscoLS1010SubModuleHwVersion_Type())
ciscoLS1010SubModuleHwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleHwVersion.setStatus(_B)
_CiscoLS1010SubModuleSwVersion_Type=Integer32
_CiscoLS1010SubModuleSwVersion_Object=MibTableColumn
ciscoLS1010SubModuleSwVersion=_CiscoLS1010SubModuleSwVersion_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,5),_CiscoLS1010SubModuleSwVersion_Type())
ciscoLS1010SubModuleSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleSwVersion.setStatus(_B)
_CiscoLS1010SubModuleDescr_Type=DisplayString
_CiscoLS1010SubModuleDescr_Object=MibTableColumn
ciscoLS1010SubModuleDescr=_CiscoLS1010SubModuleDescr_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,6),_CiscoLS1010SubModuleDescr_Type())
ciscoLS1010SubModuleDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleDescr.setStatus(_B)
class _CiscoLS1010SubModuleNumPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoLS1010SubModuleNumPorts_Type.__name__=_D
_CiscoLS1010SubModuleNumPorts_Object=MibTableColumn
ciscoLS1010SubModuleNumPorts=_CiscoLS1010SubModuleNumPorts_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,7),_CiscoLS1010SubModuleNumPorts_Type())
ciscoLS1010SubModuleNumPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleNumPorts.setStatus(_B)
class _CiscoLS1010SubModuleAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AB,1),(_H,2)))
_CiscoLS1010SubModuleAdminStatus_Type.__name__=_D
_CiscoLS1010SubModuleAdminStatus_Object=MibTableColumn
ciscoLS1010SubModuleAdminStatus=_CiscoLS1010SubModuleAdminStatus_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,8),_CiscoLS1010SubModuleAdminStatus_Type())
ciscoLS1010SubModuleAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoLS1010SubModuleAdminStatus.setStatus(_B)
_CiscoLS1010SubModuleHwVersionMinor_Type=Integer32
_CiscoLS1010SubModuleHwVersionMinor_Object=MibTableColumn
ciscoLS1010SubModuleHwVersionMinor=_CiscoLS1010SubModuleHwVersionMinor_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,9),_CiscoLS1010SubModuleHwVersionMinor_Type())
ciscoLS1010SubModuleHwVersionMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleHwVersionMinor.setStatus(_B)
_CiscoLS1010SubModuleOperStatus_Type=OperStatus
_CiscoLS1010SubModuleOperStatus_Object=MibTableColumn
ciscoLS1010SubModuleOperStatus=_CiscoLS1010SubModuleOperStatus_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,10),_CiscoLS1010SubModuleOperStatus_Type())
ciscoLS1010SubModuleOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleOperStatus.setStatus(_B)
_CiscoLS1010SubModuleSerialNumberString_Type=DisplayString
_CiscoLS1010SubModuleSerialNumberString_Object=MibTableColumn
ciscoLS1010SubModuleSerialNumberString=_CiscoLS1010SubModuleSerialNumberString_Object((1,3,6,1,4,1,9,5,11,1,3,1,1,11),_CiscoLS1010SubModuleSerialNumberString_Type())
ciscoLS1010SubModuleSerialNumberString.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010SubModuleSerialNumberString.setStatus(_B)
_CiscoLS1010PortGroup_ObjectIdentity=ObjectIdentity
ciscoLS1010PortGroup=_CiscoLS1010PortGroup_ObjectIdentity((1,3,6,1,4,1,9,5,11,1,4))
_CiscoLS1010PortTable_Object=MibTable
ciscoLS1010PortTable=_CiscoLS1010PortTable_Object((1,3,6,1,4,1,9,5,11,1,4,1))
if mibBuilder.loadTexts:ciscoLS1010PortTable.setStatus(_B)
_CiscoLS1010PortEntry_Object=MibTableRow
ciscoLS1010PortEntry=_CiscoLS1010PortEntry_Object((1,3,6,1,4,1,9,5,11,1,4,1,1))
ciscoLS1010PortEntry.setIndexNames((0,_A,_R),(0,_A,_AD),(0,_A,_AP))
if mibBuilder.loadTexts:ciscoLS1010PortEntry.setStatus(_B)
class _CiscoLS1010PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoLS1010PortIndex_Type.__name__=_D
_CiscoLS1010PortIndex_Object=MibTableColumn
ciscoLS1010PortIndex=_CiscoLS1010PortIndex_Object((1,3,6,1,4,1,9,5,11,1,4,1,1,1),_CiscoLS1010PortIndex_Type())
ciscoLS1010PortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoLS1010PortIndex.setStatus(_B)
_CiscoLS1010PortIfIndex_Type=InterfaceIndex
_CiscoLS1010PortIfIndex_Object=MibTableColumn
ciscoLS1010PortIfIndex=_CiscoLS1010PortIfIndex_Object((1,3,6,1,4,1,9,5,11,1,4,1,1,2),_CiscoLS1010PortIfIndex_Type())
ciscoLS1010PortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoLS1010PortIfIndex.setStatus(_B)
_CiscoLS1010CpuSwitchGroup_ObjectIdentity=ObjectIdentity
ciscoLS1010CpuSwitchGroup=_CiscoLS1010CpuSwitchGroup_ObjectIdentity((1,3,6,1,4,1,9,5,11,1,5))
class _CiscoAtmCpuAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AB,1),(_H,2)))
_CiscoAtmCpuAdminStatus_Type.__name__=_D
_CiscoAtmCpuAdminStatus_Object=MibScalar
ciscoAtmCpuAdminStatus=_CiscoAtmCpuAdminStatus_Object((1,3,6,1,4,1,9,5,11,1,5,1),_CiscoAtmCpuAdminStatus_Type())
ciscoAtmCpuAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmCpuAdminStatus.setStatus(_B)
_CiscoAtmSwitchTotalBuffer_Type=Integer32
_CiscoAtmSwitchTotalBuffer_Object=MibScalar
ciscoAtmSwitchTotalBuffer=_CiscoAtmSwitchTotalBuffer_Object((1,3,6,1,4,1,9,5,11,1,5,2),_CiscoAtmSwitchTotalBuffer_Type())
ciscoAtmSwitchTotalBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmSwitchTotalBuffer.setStatus(_B)
_CiscoAtmSwitchFreeBuffer_Type=Gauge32
_CiscoAtmSwitchFreeBuffer_Object=MibScalar
ciscoAtmSwitchFreeBuffer=_CiscoAtmSwitchFreeBuffer_Object((1,3,6,1,4,1,9,5,11,1,5,3),_CiscoAtmSwitchFreeBuffer_Type())
ciscoAtmSwitchFreeBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmSwitchFreeBuffer.setStatus(_B)
_CiscoAtmSwitchDiscardCells_Type=Counter32
_CiscoAtmSwitchDiscardCells_Object=MibScalar
ciscoAtmSwitchDiscardCells=_CiscoAtmSwitchDiscardCells_Object((1,3,6,1,4,1,9,5,11,1,5,4),_CiscoAtmSwitchDiscardCells_Type())
ciscoAtmSwitchDiscardCells.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmSwitchDiscardCells.setStatus(_B)
_CiscoAtmSwitchInvalidCells_Type=Counter32
_CiscoAtmSwitchInvalidCells_Object=MibScalar
ciscoAtmSwitchInvalidCells=_CiscoAtmSwitchInvalidCells_Object((1,3,6,1,4,1,9,5,11,1,5,5),_CiscoAtmSwitchInvalidCells_Type())
ciscoAtmSwitchInvalidCells.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmSwitchInvalidCells.setStatus(_B)
_CiscoAtmSwitchInvalidCellHeaderTable_Object=MibTable
ciscoAtmSwitchInvalidCellHeaderTable=_CiscoAtmSwitchInvalidCellHeaderTable_Object((1,3,6,1,4,1,9,5,11,1,5,6))
if mibBuilder.loadTexts:ciscoAtmSwitchInvalidCellHeaderTable.setStatus(_B)
_CiscoAtmSwitchInvalidCellHeaderEntry_Object=MibTableRow
ciscoAtmSwitchInvalidCellHeaderEntry=_CiscoAtmSwitchInvalidCellHeaderEntry_Object((1,3,6,1,4,1,9,5,11,1,5,6,1))
ciscoAtmSwitchInvalidCellHeaderEntry.setIndexNames((0,_A,_AQ))
if mibBuilder.loadTexts:ciscoAtmSwitchInvalidCellHeaderEntry.setStatus(_B)
class _CiscoAtmSwitchInvalidCellHeaderIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CiscoAtmSwitchInvalidCellHeaderIndex_Type.__name__=_D
_CiscoAtmSwitchInvalidCellHeaderIndex_Object=MibTableColumn
ciscoAtmSwitchInvalidCellHeaderIndex=_CiscoAtmSwitchInvalidCellHeaderIndex_Object((1,3,6,1,4,1,9,5,11,1,5,6,1,1),_CiscoAtmSwitchInvalidCellHeaderIndex_Type())
ciscoAtmSwitchInvalidCellHeaderIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoAtmSwitchInvalidCellHeaderIndex.setStatus(_B)
class _CiscoAtmSwitchInvalidCellHeader_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_CiscoAtmSwitchInvalidCellHeader_Type.__name__=_AI
_CiscoAtmSwitchInvalidCellHeader_Object=MibTableColumn
ciscoAtmSwitchInvalidCellHeader=_CiscoAtmSwitchInvalidCellHeader_Object((1,3,6,1,4,1,9,5,11,1,5,6,1,2),_CiscoAtmSwitchInvalidCellHeader_Type())
ciscoAtmSwitchInvalidCellHeader.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmSwitchInvalidCellHeader.setStatus(_B)
class _CiscoAtmCpuTerminateOamFlow_Type(TruthValue):defaultValue=2
_CiscoAtmCpuTerminateOamFlow_Type.__name__=_AA
_CiscoAtmCpuTerminateOamFlow_Object=MibScalar
ciscoAtmCpuTerminateOamFlow=_CiscoAtmCpuTerminateOamFlow_Object((1,3,6,1,4,1,9,5,11,1,5,7),_CiscoAtmCpuTerminateOamFlow_Type())
ciscoAtmCpuTerminateOamFlow.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmCpuTerminateOamFlow.setStatus(_G)
class _CiscoAtmInterceptEndToEndOamFlow_Type(TruthValue):defaultValue=1
_CiscoAtmInterceptEndToEndOamFlow_Type.__name__=_AA
_CiscoAtmInterceptEndToEndOamFlow_Object=MibScalar
ciscoAtmInterceptEndToEndOamFlow=_CiscoAtmInterceptEndToEndOamFlow_Object((1,3,6,1,4,1,9,5,11,1,5,8),_CiscoAtmInterceptEndToEndOamFlow_Type())
ciscoAtmInterceptEndToEndOamFlow.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmInterceptEndToEndOamFlow.setStatus(_B)
_ClsEnetPortGroup_ObjectIdentity=ObjectIdentity
clsEnetPortGroup=_ClsEnetPortGroup_ObjectIdentity((1,3,6,1,4,1,9,5,11,1,6))
_ClsEnetPortTable_Object=MibTable
clsEnetPortTable=_ClsEnetPortTable_Object((1,3,6,1,4,1,9,5,11,1,6,1))
if mibBuilder.loadTexts:clsEnetPortTable.setStatus(_B)
_ClsEnetPortEntry_Object=MibTableRow
clsEnetPortEntry=_ClsEnetPortEntry_Object((1,3,6,1,4,1,9,5,11,1,6,1,1))
clsEnetPortEntry.setIndexNames((0,_A8,_A9))
if mibBuilder.loadTexts:clsEnetPortEntry.setStatus(_B)
class _ClsEnetPortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('auto',2),('half',3),('full',4)))
_ClsEnetPortDuplex_Type.__name__=_D
_ClsEnetPortDuplex_Object=MibTableColumn
clsEnetPortDuplex=_ClsEnetPortDuplex_Object((1,3,6,1,4,1,9,5,11,1,6,1,1,1),_ClsEnetPortDuplex_Type())
clsEnetPortDuplex.setMaxAccess(_E)
if mibBuilder.loadTexts:clsEnetPortDuplex.setStatus(_B)
class _ClsEnetPortAdminSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('auto',2),('e10Mbps',3),('e100Mbps',4),('e1000Mbps',5)))
_ClsEnetPortAdminSpeed_Type.__name__=_D
_ClsEnetPortAdminSpeed_Object=MibTableColumn
clsEnetPortAdminSpeed=_ClsEnetPortAdminSpeed_Object((1,3,6,1,4,1,9,5,11,1,6,1,1,2),_ClsEnetPortAdminSpeed_Type())
clsEnetPortAdminSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:clsEnetPortAdminSpeed.setStatus(_B)
class _ClsEnetPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('e100BaseTX',2),('e100BaseFX',3),('e1000BaseLX',4),('e1000BaseSX',5),(_P,6)))
_ClsEnetPortType_Type.__name__=_D
_ClsEnetPortType_Object=MibTableColumn
clsEnetPortType=_ClsEnetPortType_Object((1,3,6,1,4,1,9,5,11,1,6,1,1,3),_ClsEnetPortType_Type())
clsEnetPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:clsEnetPortType.setStatus(_B)
class _ClsEnetPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('autoNegotiate',2),('forceUp',3)))
_ClsEnetPortLinkStatus_Type.__name__=_D
_ClsEnetPortLinkStatus_Object=MibTableColumn
clsEnetPortLinkStatus=_ClsEnetPortLinkStatus_Object((1,3,6,1,4,1,9,5,11,1,6,1,1,4),_ClsEnetPortLinkStatus_Type())
clsEnetPortLinkStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:clsEnetPortLinkStatus.setStatus(_B)
_ClsPortLedGroup_ObjectIdentity=ObjectIdentity
clsPortLedGroup=_ClsPortLedGroup_ObjectIdentity((1,3,6,1,4,1,9,5,11,1,7))
_ClsPortLedTable_Object=MibTable
clsPortLedTable=_ClsPortLedTable_Object((1,3,6,1,4,1,9,5,11,1,7,1))
if mibBuilder.loadTexts:clsPortLedTable.setStatus(_B)
_ClsPortLedEntry_Object=MibTableRow
clsPortLedEntry=_ClsPortLedEntry_Object((1,3,6,1,4,1,9,5,11,1,7,1,1))
clsPortLedEntry.setIndexNames((0,_A8,_A9),(0,_A,_AR))
if mibBuilder.loadTexts:clsPortLedEntry.setStatus(_B)
class _ClsPortLedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ClsPortLedIndex_Type.__name__=_D
_ClsPortLedIndex_Object=MibTableColumn
clsPortLedIndex=_ClsPortLedIndex_Object((1,3,6,1,4,1,9,5,11,1,7,1,1,1),_ClsPortLedIndex_Type())
clsPortLedIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:clsPortLedIndex.setStatus(_B)
class _ClsPortLedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('ledTx',1),('ledRx',2),('ledLink',3),('led100Mbps',4),('ledRxLoss',5),('ledRxFullOut',6),('ledRxSync',7),('ledFullDuplex',8),('ledOptDetect',9)))
_ClsPortLedType_Type.__name__=_D
_ClsPortLedType_Object=MibTableColumn
clsPortLedType=_ClsPortLedType_Object((1,3,6,1,4,1,9,5,11,1,7,1,1,2),_ClsPortLedType_Type())
clsPortLedType.setMaxAccess(_C)
if mibBuilder.loadTexts:clsPortLedType.setStatus(_B)
class _ClsPortLedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('on',2),('off',3)))
_ClsPortLedStatus_Type.__name__=_D
_ClsPortLedStatus_Object=MibTableColumn
clsPortLedStatus=_ClsPortLedStatus_Object((1,3,6,1,4,1,9,5,11,1,7,1,1,3),_ClsPortLedStatus_Type())
clsPortLedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clsPortLedStatus.setStatus(_B)
_CiscoLS1010ChassisMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoLS1010ChassisMIBNotificationPrefix=_CiscoLS1010ChassisMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,5,11,2))
_CiscoLS1010ChassisMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoLS1010ChassisMIBNotifications=_CiscoLS1010ChassisMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,5,11,2,0))
_CiscoLS1010ChassisMIBConformance_ObjectIdentity=ObjectIdentity
ciscoLS1010ChassisMIBConformance=_CiscoLS1010ChassisMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,5,11,3))
_CiscoLS1010ChassisMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLS1010ChassisMIBCompliances=_CiscoLS1010ChassisMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,5,11,3,1))
_CiscoLS1010ChassisMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLS1010ChassisMIBGroups=_CiscoLS1010ChassisMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,5,11,3,2))
ciscoLS1010ChassisMIBGroup=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,1))
ciscoLS1010ChassisMIBGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_K),(_A,_W),(_A,_X),(_A,_Y),(_A,_L),(_A,_Z),(_A,_M),(_A,_a),(_A,_b),(_A,_c),(_A,_N),(_A,_O),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_AE),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_AF),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBGroup.setStatus(_G)
ciscoLS1010ChassisMIBObsoleteGroup=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,2))
ciscoLS1010ChassisMIBObsoleteGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBObsoleteGroup.setStatus(_G)
ciscoLS1010ChassisMIBRev1Group=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,3))
ciscoLS1010ChassisMIBRev1Group.setObjects((_A,_A4))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBRev1Group.setStatus(_B)
ciscoLS1010ChassisMIBClockingGroup=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,4))
ciscoLS1010ChassisMIBClockingGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBClockingGroup.setStatus(_B)
ciscoLS1010ChassisMIBGroup1=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,5))
ciscoLS1010ChassisMIBGroup1.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_K),(_A,_W),(_A,_X),(_A,_Y),(_A,_L),(_A,_Z),(_A,_M),(_A,_a),(_A,_b),(_A,_c),(_A,_N),(_A,_O),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_A5),(_A,_A4),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_AG)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBGroup1.setStatus(_G)
clsEnetPortGroup1=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,6))
clsEnetPortGroup1.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:clsEnetPortGroup1.setStatus(_B)
clsPortLedGroup1=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,7))
clsPortLedGroup1.setObjects(*((_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:clsPortLedGroup1.setStatus(_B)
clsOperStatusGroup=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,8))
clsOperStatusGroup.setObjects(*((_A,_AF),(_A,_A5)))
if mibBuilder.loadTexts:clsOperStatusGroup.setStatus(_B)
clsInletTempGroup=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,9))
clsInletTempGroup.setObjects((_A,_AE))
if mibBuilder.loadTexts:clsInletTempGroup.setStatus(_B)
ciscoLS1010ChassisMIBGroup2=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,10))
ciscoLS1010ChassisMIBGroup2.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_K),(_A,_W),(_A,_X),(_A,_Y),(_A,_L),(_A,_Z),(_A,_M),(_A,_a),(_A,_b),(_A,_c),(_A,_N),(_A,_O),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_A5),(_A,_A4),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_AG),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBGroup2.setStatus(_B)
ciscoLS1010ChassisMIBDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,9,5,11,3,2,11))
ciscoLS1010ChassisMIBDeprecatedGroup.setObjects(*((_A,_k),(_A,_r)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBDeprecatedGroup.setStatus(_AC)
ciscoLS1010ChassisFailureNotification=NotificationType((1,3,6,1,4,1,9,5,11,2,0,1))
ciscoLS1010ChassisFailureNotification.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoLS1010ChassisFailureNotification.setStatus(_B)
ciscoLS1010ChassisChangeNotification=NotificationType((1,3,6,1,4,1,9,5,11,2,0,2))
if mibBuilder.loadTexts:ciscoLS1010ChassisChangeNotification.setStatus(_B)
ciscoLS1010ChassisMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,5,11,3,2,12))
ciscoLS1010ChassisMIBNotificationGroup.setObjects(*((_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBNotificationGroup.setStatus(_B)
ciscoLS1010ChassisMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,5,11,3,1,1))
ciscoLS1010ChassisMIBCompliance.setObjects((_A,_A6))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBCompliance.setStatus(_G)
ciscoLS1010ChassisMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,5,11,3,1,2))
ciscoLS1010ChassisMIBComplianceRev1.setObjects(*((_A,_A6),(_A,_AH)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBComplianceRev1.setStatus(_G)
ciscoLS1010ChassisMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,5,11,3,1,3))
ciscoLS1010ChassisMIBComplianceRev2.setObjects(*((_A,_A6),(_A,_AH),(_A,_I)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBComplianceRev2.setStatus(_G)
ciscoLS1010ChassisMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,5,11,3,1,4))
ciscoLS1010ChassisMIBComplianceRev3.setObjects(*((_A,_A7),(_A,_I)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBComplianceRev3.setStatus(_G)
ciscoLS1010ChassisMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,5,11,3,1,5))
ciscoLS1010ChassisMIBComplianceRev4.setObjects(*((_A,_A7),(_A,_I),(_A,_Ah),(_A,_Ai)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBComplianceRev4.setStatus(_G)
ciscoLS1010ChassisMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,5,11,3,1,6))
ciscoLS1010ChassisMIBComplianceRev5.setObjects(*((_A,_A7),(_A,_I),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBComplianceRev5.setStatus(_G)
ciscoLS1010ChassisMIBComplianceRev6=ModuleCompliance((1,3,6,1,4,1,9,5,11,3,1,7))
ciscoLS1010ChassisMIBComplianceRev6.setObjects(*((_A,_Al),(_A,_I)))
if mibBuilder.loadTexts:ciscoLS1010ChassisMIBComplianceRev6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PsType':PsType,'OperStatus':OperStatus,'AdminStatus':AdminStatus,'Led':Led,'PcmciaType':PcmciaType,'ciscoLS1010ChassisMIB':ciscoLS1010ChassisMIB,'ciscoLS1010ChassisMIBObjects':ciscoLS1010ChassisMIBObjects,'ciscoLS1010ChassisGroup':ciscoLS1010ChassisGroup,_S:ciscoLS1010ChassisSysType,_T:ciscoLS1010ChassisBkplType,_U:ciscoLS1010ChassisPs0Type,_V:ciscoLS1010ChassisPs0AdminStatus,_K:ciscoLS1010ChassisPs0Status,_W:ciscoLS1010ChassisPs0Led,_X:ciscoLS1010ChassisPs1Type,_Y:ciscoLS1010ChassisPs1AdminStatus,_L:ciscoLS1010ChassisPs1Status,_Z:ciscoLS1010ChassisPs1Led,_M:ciscoLS1010ChassisFanStatus,_a:ciscoLS1010ChassisFanLed,_b:ciscoLS1010ChassisCardStatusLed,_c:ciscoLS1010ChassisEnetLinkLed,_N:ciscoLS1010Chassis12VoltStatus,_O:ciscoLS1010ChassisTempStatus,_d:ciscoLS1010ChassisPcmciaSlot0Type,_e:ciscoLS1010ChassisPcmciaSlot1Type,_f:ciscoLS1010ChassisNumSlots,_g:ciscoLS1010ChassisLastChange,_h:ciscoLS1010ChassisFailureAction,_i:ciscoLS1010ChassisChangeAction,_AT:ciscoLS1010ChassisClockingMode,_AU:ciscols1010SystemClockSourceStatus,_AV:ciscols1010SystemClockSourcePriority,_AE:ciscoLS1010ChassisInletTempStatus,'ciscoLS1010ModuleGroup':ciscoLS1010ModuleGroup,'ciscoLS1010ModuleTable':ciscoLS1010ModuleTable,'ciscoLS1010ModuleEntry':ciscoLS1010ModuleEntry,_R:ciscoLS1010ModuleIndex,_j:ciscoLS1010ModuleType,_k:ciscoLS1010ModuleSerialNumber,_l:ciscoLS1010ModuleHwVersion,_m:ciscoLS1010ModuleSwVersion,_n:ciscoLS1010ModuleDescr,_o:ciscoLS1010ModuleNumSubModules,_p:ciscoLS1010ModuleAdminStatus,_AF:ciscoLS1010ModuleOperStatus,_Ac:ciscoLS1010ModuleHwVersionMinor,_Ad:ciscoLS1010ModuleSerialNumberString,'ciscoLS1010SubModuleGroup':ciscoLS1010SubModuleGroup,'ciscoLS1010SubModuleTable':ciscoLS1010SubModuleTable,'ciscoLS1010SubModuleEntry':ciscoLS1010SubModuleEntry,_AD:ciscoLS1010SubModuleIndex,_q:ciscoLS1010SubModuleType,_r:ciscoLS1010SubModuleSerialNumber,_s:ciscoLS1010SubModuleHwVersion,_t:ciscoLS1010SubModuleSwVersion,_u:ciscoLS1010SubModuleDescr,_v:ciscoLS1010SubModuleNumPorts,_w:ciscoLS1010SubModuleAdminStatus,_A4:ciscoLS1010SubModuleHwVersionMinor,_A5:ciscoLS1010SubModuleOperStatus,_Ae:ciscoLS1010SubModuleSerialNumberString,'ciscoLS1010PortGroup':ciscoLS1010PortGroup,'ciscoLS1010PortTable':ciscoLS1010PortTable,'ciscoLS1010PortEntry':ciscoLS1010PortEntry,_AP:ciscoLS1010PortIndex,_x:ciscoLS1010PortIfIndex,'ciscoLS1010CpuSwitchGroup':ciscoLS1010CpuSwitchGroup,_y:ciscoAtmCpuAdminStatus,_z:ciscoAtmSwitchTotalBuffer,_A0:ciscoAtmSwitchFreeBuffer,_A1:ciscoAtmSwitchDiscardCells,_A2:ciscoAtmSwitchInvalidCells,'ciscoAtmSwitchInvalidCellHeaderTable':ciscoAtmSwitchInvalidCellHeaderTable,'ciscoAtmSwitchInvalidCellHeaderEntry':ciscoAtmSwitchInvalidCellHeaderEntry,_AQ:ciscoAtmSwitchInvalidCellHeaderIndex,_A3:ciscoAtmSwitchInvalidCellHeader,_AS:ciscoAtmCpuTerminateOamFlow,_AG:ciscoAtmInterceptEndToEndOamFlow,'clsEnetPortGroup':clsEnetPortGroup,'clsEnetPortTable':clsEnetPortTable,'clsEnetPortEntry':clsEnetPortEntry,_AW:clsEnetPortDuplex,_AX:clsEnetPortAdminSpeed,_AY:clsEnetPortType,_AZ:clsEnetPortLinkStatus,'clsPortLedGroup':clsPortLedGroup,'clsPortLedTable':clsPortLedTable,'clsPortLedEntry':clsPortLedEntry,_AR:clsPortLedIndex,_Aa:clsPortLedType,_Ab:clsPortLedStatus,'ciscoLS1010ChassisMIBNotificationPrefix':ciscoLS1010ChassisMIBNotificationPrefix,'ciscoLS1010ChassisMIBNotifications':ciscoLS1010ChassisMIBNotifications,_Af:ciscoLS1010ChassisFailureNotification,_Ag:ciscoLS1010ChassisChangeNotification,'ciscoLS1010ChassisMIBConformance':ciscoLS1010ChassisMIBConformance,'ciscoLS1010ChassisMIBCompliances':ciscoLS1010ChassisMIBCompliances,'ciscoLS1010ChassisMIBCompliance':ciscoLS1010ChassisMIBCompliance,'ciscoLS1010ChassisMIBComplianceRev1':ciscoLS1010ChassisMIBComplianceRev1,'ciscoLS1010ChassisMIBComplianceRev2':ciscoLS1010ChassisMIBComplianceRev2,'ciscoLS1010ChassisMIBComplianceRev3':ciscoLS1010ChassisMIBComplianceRev3,'ciscoLS1010ChassisMIBComplianceRev4':ciscoLS1010ChassisMIBComplianceRev4,'ciscoLS1010ChassisMIBComplianceRev5':ciscoLS1010ChassisMIBComplianceRev5,'ciscoLS1010ChassisMIBComplianceRev6':ciscoLS1010ChassisMIBComplianceRev6,'ciscoLS1010ChassisMIBGroups':ciscoLS1010ChassisMIBGroups,_A6:ciscoLS1010ChassisMIBGroup,'ciscoLS1010ChassisMIBObsoleteGroup':ciscoLS1010ChassisMIBObsoleteGroup,_AH:ciscoLS1010ChassisMIBRev1Group,_I:ciscoLS1010ChassisMIBClockingGroup,_A7:ciscoLS1010ChassisMIBGroup1,_Ah:clsEnetPortGroup1,_Ai:clsPortLedGroup1,_Aj:clsOperStatusGroup,_Ak:clsInletTempGroup,_Al:ciscoLS1010ChassisMIBGroup2,'ciscoLS1010ChassisMIBDeprecatedGroup':ciscoLS1010ChassisMIBDeprecatedGroup,'ciscoLS1010ChassisMIBNotificationGroup':ciscoLS1010ChassisMIBNotificationGroup})