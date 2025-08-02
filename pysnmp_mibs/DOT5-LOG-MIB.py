_d='tRingPortRingPortGrpId'
_c='tRingPortRingPortId'
_b='tRingPortStnPortGrpId'
_a='tRingPortStnPortId'
_Z='tRingPortMgmtPortGrpId'
_Y='tRingPortMgmtPortId'
_X='ringOut'
_W='ringIn'
_V='notApplicable'
_U='tRingPortGrpId'
_T='tRingAlarmsStnThrshAddress'
_S='tRingAlarmsStnEnblAddress'
_R='tRingStatsStnAddress'
_Q='tRingMgmtSecurityStnAddress'
_P='tRingMgmtSecurityIfIndex'
_O='tRingMgmtStnAddress'
_N='invalid'
_M='beaconing'
_L='faultDetected'
_K='noFaultDetected'
_J='noEnable'
_I='DisplayString'
_H='DOT5-LOG-MIB'
_G='OctetString'
_F='disable'
_E='enable'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot5,=mibBuilder.importSymbols('CTRON-MIB-NAMES','dot5')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
_Dot5Rev1_ObjectIdentity=ObjectIdentity
dot5Rev1=_Dot5Rev1_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1))
_TRing_ObjectIdentity=ObjectIdentity
tRing=_TRing_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1))
_TRingMgmt_ObjectIdentity=ObjectIdentity
tRingMgmt=_TRingMgmt_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,1))
_TRingMgmtRing_ObjectIdentity=ObjectIdentity
tRingMgmtRing=_TRingMgmtRing_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1))
class _TRingMgmtRingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_TRingMgmtRingName_Type.__name__=_I
_TRingMgmtRingName_Object=MibScalar
tRingMgmtRingName=_TRingMgmtRingName_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,1),_TRingMgmtRingName_Type())
tRingMgmtRingName.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtRingName.setStatus(_A)
_TRingMgmtStnPortCount_Type=Integer32
_TRingMgmtStnPortCount_Object=MibScalar
tRingMgmtStnPortCount=_TRingMgmtStnPortCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,2),_TRingMgmtStnPortCount_Type())
tRingMgmtStnPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtStnPortCount.setStatus(_A)
_TRingMgmtRingPortCount_Type=Integer32
_TRingMgmtRingPortCount_Object=MibScalar
tRingMgmtRingPortCount=_TRingMgmtRingPortCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,3),_TRingMgmtRingPortCount_Type())
tRingMgmtRingPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtRingPortCount.setStatus(_A)
class _TRingMgmtStnPortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_E,2)))
_TRingMgmtStnPortsEnable_Type.__name__=_D
_TRingMgmtStnPortsEnable_Object=MibScalar
tRingMgmtStnPortsEnable=_TRingMgmtStnPortsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,4),_TRingMgmtStnPortsEnable_Type())
tRingMgmtStnPortsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtStnPortsEnable.setStatus(_A)
class _TRingMgmtRingPortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_E,2)))
_TRingMgmtRingPortsEnable_Type.__name__=_D
_TRingMgmtRingPortsEnable_Object=MibScalar
tRingMgmtRingPortsEnable=_TRingMgmtRingPortsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,5),_TRingMgmtRingPortsEnable_Type())
tRingMgmtRingPortsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtRingPortsEnable.setStatus(_A)
_TRingMgmtStnPortsOn_Type=Integer32
_TRingMgmtStnPortsOn_Object=MibScalar
tRingMgmtStnPortsOn=_TRingMgmtStnPortsOn_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,6),_TRingMgmtStnPortsOn_Type())
tRingMgmtStnPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtStnPortsOn.setStatus(_A)
_TRingMgmtRingPortsOn_Type=Integer32
_TRingMgmtRingPortsOn_Object=MibScalar
tRingMgmtRingPortsOn=_TRingMgmtRingPortsOn_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,7),_TRingMgmtRingPortsOn_Type())
tRingMgmtRingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtRingPortsOn.setStatus(_A)
_TRingMgmtStations_Type=Integer32
_TRingMgmtStations_Object=MibScalar
tRingMgmtStations=_TRingMgmtStations_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,8),_TRingMgmtStations_Type())
tRingMgmtStations.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtStations.setStatus(_A)
class _TRingMgmtRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('closed',2),('normalTokenProtocols',3),('purge',4),('contention',5),(_M,6),('lobeFail',7),('ringPollFailure',8)))
_TRingMgmtRingState_Type.__name__=_D
_TRingMgmtRingState_Object=MibScalar
tRingMgmtRingState=_TRingMgmtRingState_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,9),_TRingMgmtRingState_Type())
tRingMgmtRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtRingState.setStatus(_A)
_TRingMgmtRingSpeed_Type=Integer32
_TRingMgmtRingSpeed_Object=MibScalar
tRingMgmtRingSpeed=_TRingMgmtRingSpeed_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,10),_TRingMgmtRingSpeed_Type())
tRingMgmtRingSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtRingSpeed.setStatus(_A)
class _TRingMgmtActiveMonitor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingMgmtActiveMonitor_Type.__name__=_G
_TRingMgmtActiveMonitor_Object=MibScalar
tRingMgmtActiveMonitor=_TRingMgmtActiveMonitor_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,11),_TRingMgmtActiveMonitor_Type())
tRingMgmtActiveMonitor.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtActiveMonitor.setStatus(_A)
_TRingMgmtRingNumber_Type=Integer32
_TRingMgmtRingNumber_Object=MibScalar
tRingMgmtRingNumber=_TRingMgmtRingNumber_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,12),_TRingMgmtRingNumber_Type())
tRingMgmtRingNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtRingNumber.setStatus(_A)
class _TRingMgmtBeaconRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_E,2),(_N,3)))
_TRingMgmtBeaconRecovery_Type.__name__=_D
_TRingMgmtBeaconRecovery_Object=MibScalar
tRingMgmtBeaconRecovery=_TRingMgmtBeaconRecovery_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,13),_TRingMgmtBeaconRecovery_Type())
tRingMgmtBeaconRecovery.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBeaconRecovery.setStatus(_A)
class _TRingMgmtBcnRecRingPortRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_TRingMgmtBcnRecRingPortRetryCount_Type.__name__=_D
_TRingMgmtBcnRecRingPortRetryCount_Object=MibScalar
tRingMgmtBcnRecRingPortRetryCount=_TRingMgmtBcnRecRingPortRetryCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,14),_TRingMgmtBcnRecRingPortRetryCount_Type())
tRingMgmtBcnRecRingPortRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBcnRecRingPortRetryCount.setStatus(_A)
class _TRingMgmtBcnRecRingPortRetryDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_TRingMgmtBcnRecRingPortRetryDelay_Type.__name__=_D
_TRingMgmtBcnRecRingPortRetryDelay_Object=MibScalar
tRingMgmtBcnRecRingPortRetryDelay=_TRingMgmtBcnRecRingPortRetryDelay_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,15),_TRingMgmtBcnRecRingPortRetryDelay_Type())
tRingMgmtBcnRecRingPortRetryDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBcnRecRingPortRetryDelay.setStatus(_A)
class _TRingMgmtBcnRecStnPortRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_TRingMgmtBcnRecStnPortRetryCount_Type.__name__=_D
_TRingMgmtBcnRecStnPortRetryCount_Object=MibScalar
tRingMgmtBcnRecStnPortRetryCount=_TRingMgmtBcnRecStnPortRetryCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,16),_TRingMgmtBcnRecStnPortRetryCount_Type())
tRingMgmtBcnRecStnPortRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBcnRecStnPortRetryCount.setStatus(_A)
class _TRingMgmtBcnRecStnPortRetryDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_TRingMgmtBcnRecStnPortRetryDelay_Type.__name__=_D
_TRingMgmtBcnRecStnPortRetryDelay_Object=MibScalar
tRingMgmtBcnRecStnPortRetryDelay=_TRingMgmtBcnRecStnPortRetryDelay_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,17),_TRingMgmtBcnRecStnPortRetryDelay_Type())
tRingMgmtBcnRecStnPortRetryDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBcnRecStnPortRetryDelay.setStatus(_A)
class _TRingMgmtBcnRecBrdBypassRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_TRingMgmtBcnRecBrdBypassRetryCount_Type.__name__=_D
_TRingMgmtBcnRecBrdBypassRetryCount_Object=MibScalar
tRingMgmtBcnRecBrdBypassRetryCount=_TRingMgmtBcnRecBrdBypassRetryCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,18),_TRingMgmtBcnRecBrdBypassRetryCount_Type())
tRingMgmtBcnRecBrdBypassRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBcnRecBrdBypassRetryCount.setStatus(_A)
class _TRingMgmtBcnRecBrdBypassRetryDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TRingMgmtBcnRecBrdBypassRetryDelay_Type.__name__=_D
_TRingMgmtBcnRecBrdBypassRetryDelay_Object=MibScalar
tRingMgmtBcnRecBrdBypassRetryDelay=_TRingMgmtBcnRecBrdBypassRetryDelay_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,19),_TRingMgmtBcnRecBrdBypassRetryDelay_Type())
tRingMgmtBcnRecBrdBypassRetryDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBcnRecBrdBypassRetryDelay.setStatus(_A)
class _TRingMgmtBcnRecBrdWrapRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_TRingMgmtBcnRecBrdWrapRetryCount_Type.__name__=_D
_TRingMgmtBcnRecBrdWrapRetryCount_Object=MibScalar
tRingMgmtBcnRecBrdWrapRetryCount=_TRingMgmtBcnRecBrdWrapRetryCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,20),_TRingMgmtBcnRecBrdWrapRetryCount_Type())
tRingMgmtBcnRecBrdWrapRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBcnRecBrdWrapRetryCount.setStatus(_A)
class _TRingMgmtBcnRecBrdWrapRetryDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TRingMgmtBcnRecBrdWrapRetryDelay_Type.__name__=_D
_TRingMgmtBcnRecBrdWrapRetryDelay_Object=MibScalar
tRingMgmtBcnRecBrdWrapRetryDelay=_TRingMgmtBcnRecBrdWrapRetryDelay_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,21),_TRingMgmtBcnRecBrdWrapRetryDelay_Type())
tRingMgmtBcnRecBrdWrapRetryDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtBcnRecBrdWrapRetryDelay.setStatus(_A)
class _TRingMgmtRingPollRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_E,2),(_N,3)))
_TRingMgmtRingPollRecovery_Type.__name__=_D
_TRingMgmtRingPollRecovery_Object=MibScalar
tRingMgmtRingPollRecovery=_TRingMgmtRingPollRecovery_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,1,22),_TRingMgmtRingPollRecovery_Type())
tRingMgmtRingPollRecovery.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtRingPollRecovery.setStatus(_A)
_TRingMgmtStn_ObjectIdentity=ObjectIdentity
tRingMgmtStn=_TRingMgmtStn_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2))
_TRingMgmtStnTable_Object=MibTable
tRingMgmtStnTable=_TRingMgmtStnTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1))
if mibBuilder.loadTexts:tRingMgmtStnTable.setStatus(_A)
_TRingMgmtStnEntry_Object=MibTableRow
tRingMgmtStnEntry=_TRingMgmtStnEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1))
tRingMgmtStnEntry.setIndexNames((0,_H,_O))
if mibBuilder.loadTexts:tRingMgmtStnEntry.setStatus(_A)
class _TRingMgmtStnAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingMgmtStnAddress_Type.__name__=_G
_TRingMgmtStnAddress_Object=MibTableColumn
tRingMgmtStnAddress=_TRingMgmtStnAddress_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,1),_TRingMgmtStnAddress_Type())
tRingMgmtStnAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtStnAddress.setStatus(_A)
class _TRingMgmtStnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_TRingMgmtStnName_Type.__name__=_I
_TRingMgmtStnName_Object=MibTableColumn
tRingMgmtStnName=_TRingMgmtStnName_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,2),_TRingMgmtStnName_Type())
tRingMgmtStnName.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtStnName.setStatus(_A)
_TRingMgmtStnBoard_Type=Integer32
_TRingMgmtStnBoard_Object=MibTableColumn
tRingMgmtStnBoard=_TRingMgmtStnBoard_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,3),_TRingMgmtStnBoard_Type())
tRingMgmtStnBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtStnBoard.setStatus(_A)
_TRingMgmtStnPort_Type=Integer32
_TRingMgmtStnPort_Object=MibTableColumn
tRingMgmtStnPort=_TRingMgmtStnPort_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,4),_TRingMgmtStnPort_Type())
tRingMgmtStnPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtStnPort.setStatus(_A)
class _TRingMgmtStnUNA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingMgmtStnUNA_Type.__name__=_G
_TRingMgmtStnUNA_Object=MibTableColumn
tRingMgmtStnUNA=_TRingMgmtStnUNA_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,5),_TRingMgmtStnUNA_Type())
tRingMgmtStnUNA.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtStnUNA.setStatus(_A)
class _TRingMgmtStnDNA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingMgmtStnDNA_Type.__name__=_G
_TRingMgmtStnDNA_Object=MibTableColumn
tRingMgmtStnDNA=_TRingMgmtStnDNA_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,6),_TRingMgmtStnDNA_Type())
tRingMgmtStnDNA.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtStnDNA.setStatus(_A)
class _TRingMgmtStnPhysLocation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_TRingMgmtStnPhysLocation_Type.__name__=_G
_TRingMgmtStnPhysLocation_Object=MibTableColumn
tRingMgmtStnPhysLocation=_TRingMgmtStnPhysLocation_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,7),_TRingMgmtStnPhysLocation_Type())
tRingMgmtStnPhysLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtStnPhysLocation.setStatus(_A)
class _TRingMgmtStnFuncClasses_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_TRingMgmtStnFuncClasses_Type.__name__=_G
_TRingMgmtStnFuncClasses_Object=MibTableColumn
tRingMgmtStnFuncClasses=_TRingMgmtStnFuncClasses_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,8),_TRingMgmtStnFuncClasses_Type())
tRingMgmtStnFuncClasses.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtStnFuncClasses.setStatus(_A)
class _TRingMgmtStnPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_TRingMgmtStnPriority_Type.__name__=_D
_TRingMgmtStnPriority_Object=MibTableColumn
tRingMgmtStnPriority=_TRingMgmtStnPriority_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,9),_TRingMgmtStnPriority_Type())
tRingMgmtStnPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtStnPriority.setStatus(_A)
class _TRingMgmtStnRemoveStn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noRemove',1),('remove',2)))
_TRingMgmtStnRemoveStn_Type.__name__=_D
_TRingMgmtStnRemoveStn_Object=MibTableColumn
tRingMgmtStnRemoveStn=_TRingMgmtStnRemoveStn_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,2,1,1,10),_TRingMgmtStnRemoveStn_Type())
tRingMgmtStnRemoveStn.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtStnRemoveStn.setStatus(_A)
_TRingMgmtHost_ObjectIdentity=ObjectIdentity
tRingMgmtHost=_TRingMgmtHost_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,1,3))
class _TRingMgmtHostCommands_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nop',1),('hwReset',2),('swReset',3),('open',4),('close',5)))
_TRingMgmtHostCommands_Type.__name__=_D
_TRingMgmtHostCommands_Object=MibScalar
tRingMgmtHostCommands=_TRingMgmtHostCommands_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,3,1),_TRingMgmtHostCommands_Type())
tRingMgmtHostCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtHostCommands.setStatus(_A)
class _TRingMgmtHostOpenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('noOpen',1),('badParam',2),('lobeTestFailed',3),('signalLoss',4),('insertionTimeout',5),('ringFailed',6),(_M,7),('duplicateMACAddress',8),('requestFailed',9),('removeReceived',10),('open',11)))
_TRingMgmtHostOpenStatus_Type.__name__=_D
_TRingMgmtHostOpenStatus_Object=MibScalar
tRingMgmtHostOpenStatus=_TRingMgmtHostOpenStatus_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,3,2),_TRingMgmtHostOpenStatus_Type())
tRingMgmtHostOpenStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtHostOpenStatus.setStatus(_A)
_TRingMgmtHostErrorStatus_Type=Integer32
_TRingMgmtHostErrorStatus_Object=MibScalar
tRingMgmtHostErrorStatus=_TRingMgmtHostErrorStatus_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,3,3),_TRingMgmtHostErrorStatus_Type())
tRingMgmtHostErrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtHostErrorStatus.setStatus(_A)
class _TRingMgmtHostAMContention_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noContentionAllowed',1),('contentionAllowed',2)))
_TRingMgmtHostAMContention_Type.__name__=_D
_TRingMgmtHostAMContention_Object=MibScalar
tRingMgmtHostAMContention=_TRingMgmtHostAMContention_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,3,4),_TRingMgmtHostAMContention_Type())
tRingMgmtHostAMContention.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtHostAMContention.setStatus(_A)
_TRingMgmtHostTErrorReport_Type=Integer32
_TRingMgmtHostTErrorReport_Object=MibScalar
tRingMgmtHostTErrorReport=_TRingMgmtHostTErrorReport_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,3,5),_TRingMgmtHostTErrorReport_Type())
tRingMgmtHostTErrorReport.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtHostTErrorReport.setStatus(_A)
class _TRingMgmtHostLocalAdminMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingMgmtHostLocalAdminMac_Type.__name__=_G
_TRingMgmtHostLocalAdminMac_Object=MibScalar
tRingMgmtHostLocalAdminMac=_TRingMgmtHostLocalAdminMac_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,3,6),_TRingMgmtHostLocalAdminMac_Type())
tRingMgmtHostLocalAdminMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtHostLocalAdminMac.setStatus('deprecated')
_TRingMgmtSecurity_ObjectIdentity=ObjectIdentity
tRingMgmtSecurity=_TRingMgmtSecurity_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4))
class _TRingMgmtSecurityAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('enableWithAlarm',2),('enableWithRemoveAndAlarm',3)))
_TRingMgmtSecurityAdminState_Type.__name__=_D
_TRingMgmtSecurityAdminState_Object=MibScalar
tRingMgmtSecurityAdminState=_TRingMgmtSecurityAdminState_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4,1),_TRingMgmtSecurityAdminState_Type())
tRingMgmtSecurityAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtSecurityAdminState.setStatus(_A)
class _TRingMgmtSecurityAddressAdd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingMgmtSecurityAddressAdd_Type.__name__=_G
_TRingMgmtSecurityAddressAdd_Object=MibScalar
tRingMgmtSecurityAddressAdd=_TRingMgmtSecurityAddressAdd_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4,2),_TRingMgmtSecurityAddressAdd_Type())
tRingMgmtSecurityAddressAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtSecurityAddressAdd.setStatus(_A)
class _TRingMgmtSecurityAddressRemove_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingMgmtSecurityAddressRemove_Type.__name__=_G
_TRingMgmtSecurityAddressRemove_Object=MibScalar
tRingMgmtSecurityAddressRemove=_TRingMgmtSecurityAddressRemove_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4,3),_TRingMgmtSecurityAddressRemove_Type())
tRingMgmtSecurityAddressRemove.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingMgmtSecurityAddressRemove.setStatus(_A)
_TRingMgmtSecurityStnCount_Type=Integer32
_TRingMgmtSecurityStnCount_Object=MibScalar
tRingMgmtSecurityStnCount=_TRingMgmtSecurityStnCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4,4),_TRingMgmtSecurityStnCount_Type())
tRingMgmtSecurityStnCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtSecurityStnCount.setStatus(_A)
_TRingMgmtSecurityTable_Object=MibTable
tRingMgmtSecurityTable=_TRingMgmtSecurityTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4,5))
if mibBuilder.loadTexts:tRingMgmtSecurityTable.setStatus(_A)
_TRingMgmtSecurityEntry_Object=MibTableRow
tRingMgmtSecurityEntry=_TRingMgmtSecurityEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4,5,1))
tRingMgmtSecurityEntry.setIndexNames((0,_H,_P),(0,_H,_Q))
if mibBuilder.loadTexts:tRingMgmtSecurityEntry.setStatus(_A)
_TRingMgmtSecurityIfIndex_Type=Integer32
_TRingMgmtSecurityIfIndex_Object=MibTableColumn
tRingMgmtSecurityIfIndex=_TRingMgmtSecurityIfIndex_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4,5,1,1),_TRingMgmtSecurityIfIndex_Type())
tRingMgmtSecurityIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtSecurityIfIndex.setStatus(_A)
class _TRingMgmtSecurityStnAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingMgmtSecurityStnAddress_Type.__name__=_G
_TRingMgmtSecurityStnAddress_Object=MibTableColumn
tRingMgmtSecurityStnAddress=_TRingMgmtSecurityStnAddress_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,1,4,5,1,2),_TRingMgmtSecurityStnAddress_Type())
tRingMgmtSecurityStnAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingMgmtSecurityStnAddress.setStatus(_A)
_TRingStats_ObjectIdentity=ObjectIdentity
tRingStats=_TRingStats_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,2))
_TRingStatsRing_ObjectIdentity=ObjectIdentity
tRingStatsRing=_TRingStatsRing_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1))
_TRingStatsRingErrs_ObjectIdentity=ObjectIdentity
tRingStatsRingErrs=_TRingStatsRingErrs_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1))
_TRingStatsRingFrames_Type=Counter32
_TRingStatsRingFrames_Object=MibScalar
tRingStatsRingFrames=_TRingStatsRingFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,1),_TRingStatsRingFrames_Type())
tRingStatsRingFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFrames.setStatus(_A)
_TRingStatsRingKBytes_Type=Counter32
_TRingStatsRingKBytes_Object=MibScalar
tRingStatsRingKBytes=_TRingStatsRingKBytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,2),_TRingStatsRingKBytes_Type())
tRingStatsRingKBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingKBytes.setStatus(_A)
_TRingStatsRingLineErrors_Type=Counter32
_TRingStatsRingLineErrors_Object=MibScalar
tRingStatsRingLineErrors=_TRingStatsRingLineErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,3),_TRingStatsRingLineErrors_Type())
tRingStatsRingLineErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingLineErrors.setStatus(_A)
_TRingStatsRingBurstErrors_Type=Counter32
_TRingStatsRingBurstErrors_Object=MibScalar
tRingStatsRingBurstErrors=_TRingStatsRingBurstErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,4),_TRingStatsRingBurstErrors_Type())
tRingStatsRingBurstErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingBurstErrors.setStatus(_A)
_TRingStatsRingACErrors_Type=Counter32
_TRingStatsRingACErrors_Object=MibScalar
tRingStatsRingACErrors=_TRingStatsRingACErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,5),_TRingStatsRingACErrors_Type())
tRingStatsRingACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingACErrors.setStatus(_A)
_TRingStatsRingAbortSequences_Type=Counter32
_TRingStatsRingAbortSequences_Object=MibScalar
tRingStatsRingAbortSequences=_TRingStatsRingAbortSequences_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,6),_TRingStatsRingAbortSequences_Type())
tRingStatsRingAbortSequences.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingAbortSequences.setStatus(_A)
_TRingStatsRingInternalErrors_Type=Counter32
_TRingStatsRingInternalErrors_Object=MibScalar
tRingStatsRingInternalErrors=_TRingStatsRingInternalErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,7),_TRingStatsRingInternalErrors_Type())
tRingStatsRingInternalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingInternalErrors.setStatus(_A)
_TRingStatsRingLostFrames_Type=Counter32
_TRingStatsRingLostFrames_Object=MibScalar
tRingStatsRingLostFrames=_TRingStatsRingLostFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,8),_TRingStatsRingLostFrames_Type())
tRingStatsRingLostFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingLostFrames.setStatus(_A)
_TRingStatsRingCongestErrors_Type=Counter32
_TRingStatsRingCongestErrors_Object=MibScalar
tRingStatsRingCongestErrors=_TRingStatsRingCongestErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,9),_TRingStatsRingCongestErrors_Type())
tRingStatsRingCongestErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingCongestErrors.setStatus(_A)
_TRingStatsRingFCErrors_Type=Counter32
_TRingStatsRingFCErrors_Object=MibScalar
tRingStatsRingFCErrors=_TRingStatsRingFCErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,10),_TRingStatsRingFCErrors_Type())
tRingStatsRingFCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFCErrors.setStatus(_A)
_TRingStatsRingTokenErrors_Type=Counter32
_TRingStatsRingTokenErrors_Object=MibScalar
tRingStatsRingTokenErrors=_TRingStatsRingTokenErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,11),_TRingStatsRingTokenErrors_Type())
tRingStatsRingTokenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingTokenErrors.setStatus(_A)
_TRingStatsRingFreqErrors_Type=Counter32
_TRingStatsRingFreqErrors_Object=MibScalar
tRingStatsRingFreqErrors=_TRingStatsRingFreqErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,12),_TRingStatsRingFreqErrors_Type())
tRingStatsRingFreqErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFreqErrors.setStatus(_A)
_TRingStatsRingTotalErrors_Type=Counter32
_TRingStatsRingTotalErrors_Object=MibScalar
tRingStatsRingTotalErrors=_TRingStatsRingTotalErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,13),_TRingStatsRingTotalErrors_Type())
tRingStatsRingTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingTotalErrors.setStatus(_A)
_TRingStatsRingAMChanges_Type=Counter32
_TRingStatsRingAMChanges_Object=MibScalar
tRingStatsRingAMChanges=_TRingStatsRingAMChanges_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,14),_TRingStatsRingAMChanges_Type())
tRingStatsRingAMChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingAMChanges.setStatus(_A)
_TRingStatsRingRingPurges_Type=Counter32
_TRingStatsRingRingPurges_Object=MibScalar
tRingStatsRingRingPurges=_TRingStatsRingRingPurges_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,15),_TRingStatsRingRingPurges_Type())
tRingStatsRingRingPurges.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingRingPurges.setStatus(_A)
_TRingStatsRingBeaconEvents_Type=Counter32
_TRingStatsRingBeaconEvents_Object=MibScalar
tRingStatsRingBeaconEvents=_TRingStatsRingBeaconEvents_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,16),_TRingStatsRingBeaconEvents_Type())
tRingStatsRingBeaconEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingBeaconEvents.setStatus(_A)
_TRingStatsRingLongestBeacon_Type=TimeTicks
_TRingStatsRingLongestBeacon_Object=MibScalar
tRingStatsRingLongestBeacon=_TRingStatsRingLongestBeacon_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,17),_TRingStatsRingLongestBeacon_Type())
tRingStatsRingLongestBeacon.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingLongestBeacon.setStatus(_A)
_TRingStatsRingLastBeacon_Type=TimeTicks
_TRingStatsRingLastBeacon_Object=MibScalar
tRingStatsRingLastBeacon=_TRingStatsRingLastBeacon_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,18),_TRingStatsRingLastBeacon_Type())
tRingStatsRingLastBeacon.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingLastBeacon.setStatus(_A)
class _TRingStatsRingLastBeaconType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('recoveryModeSet',1),('signalLossError',2),('streamingSignalNotClaimToken',3),('streamingSignalClaimToken',4),('noBeaconFramesDetected',5)))
_TRingStatsRingLastBeaconType_Type.__name__=_D
_TRingStatsRingLastBeaconType_Object=MibScalar
tRingStatsRingLastBeaconType=_TRingStatsRingLastBeaconType_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,19),_TRingStatsRingLastBeaconType_Type())
tRingStatsRingLastBeaconType.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingLastBeaconType.setStatus(_A)
_TRingStatsRingPollFailureNoRecovery_Type=Counter32
_TRingStatsRingPollFailureNoRecovery_Object=MibScalar
tRingStatsRingPollFailureNoRecovery=_TRingStatsRingPollFailureNoRecovery_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,20),_TRingStatsRingPollFailureNoRecovery_Type())
tRingStatsRingPollFailureNoRecovery.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingPollFailureNoRecovery.setStatus(_A)
_TRingStatsRingPollFailureNNIFrameCount_Type=Counter32
_TRingStatsRingPollFailureNNIFrameCount_Object=MibScalar
tRingStatsRingPollFailureNNIFrameCount=_TRingStatsRingPollFailureNNIFrameCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,21),_TRingStatsRingPollFailureNNIFrameCount_Type())
tRingStatsRingPollFailureNNIFrameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingPollFailureNNIFrameCount.setStatus(_A)
class _TRingStatsRingPollFailureNNIFrameAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingStatsRingPollFailureNNIFrameAddress_Type.__name__=_G
_TRingStatsRingPollFailureNNIFrameAddress_Object=MibScalar
tRingStatsRingPollFailureNNIFrameAddress=_TRingStatsRingPollFailureNNIFrameAddress_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,22),_TRingStatsRingPollFailureNNIFrameAddress_Type())
tRingStatsRingPollFailureNNIFrameAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingPollFailureNNIFrameAddress.setStatus(_A)
_TRingStatsRingPollFailureLastNNIFrameTime_Type=Counter32
_TRingStatsRingPollFailureLastNNIFrameTime_Object=MibScalar
tRingStatsRingPollFailureLastNNIFrameTime=_TRingStatsRingPollFailureLastNNIFrameTime_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,23),_TRingStatsRingPollFailureLastNNIFrameTime_Type())
tRingStatsRingPollFailureLastNNIFrameTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingPollFailureLastNNIFrameTime.setStatus(_A)
class _TRingStatsRingPollFailureLastDNAAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingStatsRingPollFailureLastDNAAddress_Type.__name__=_G
_TRingStatsRingPollFailureLastDNAAddress_Object=MibScalar
tRingStatsRingPollFailureLastDNAAddress=_TRingStatsRingPollFailureLastDNAAddress_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,1,24),_TRingStatsRingPollFailureLastDNAAddress_Type())
tRingStatsRingPollFailureLastDNAAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingPollFailureLastDNAAddress.setStatus(_A)
_TRingStatsRingProtos_ObjectIdentity=ObjectIdentity
tRingStatsRingProtos=_TRingStatsRingProtos_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2))
_TRingStatsRingProtocolSnaFrames_Type=Counter32
_TRingStatsRingProtocolSnaFrames_Object=MibScalar
tRingStatsRingProtocolSnaFrames=_TRingStatsRingProtocolSnaFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2,1),_TRingStatsRingProtocolSnaFrames_Type())
tRingStatsRingProtocolSnaFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingProtocolSnaFrames.setStatus(_A)
_TRingStatsRingProtocolXnsFrames_Type=Counter32
_TRingStatsRingProtocolXnsFrames_Object=MibScalar
tRingStatsRingProtocolXnsFrames=_TRingStatsRingProtocolXnsFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2,2),_TRingStatsRingProtocolXnsFrames_Type())
tRingStatsRingProtocolXnsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingProtocolXnsFrames.setStatus(_A)
_TRingStatsRingProtocolTcpIpFrames_Type=Counter32
_TRingStatsRingProtocolTcpIpFrames_Object=MibScalar
tRingStatsRingProtocolTcpIpFrames=_TRingStatsRingProtocolTcpIpFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2,3),_TRingStatsRingProtocolTcpIpFrames_Type())
tRingStatsRingProtocolTcpIpFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingProtocolTcpIpFrames.setStatus(_A)
_TRingStatsRingProtocolBanyanFrames_Type=Counter32
_TRingStatsRingProtocolBanyanFrames_Object=MibScalar
tRingStatsRingProtocolBanyanFrames=_TRingStatsRingProtocolBanyanFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2,4),_TRingStatsRingProtocolBanyanFrames_Type())
tRingStatsRingProtocolBanyanFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingProtocolBanyanFrames.setStatus(_A)
_TRingStatsRingProtocolIpxFrames_Type=Counter32
_TRingStatsRingProtocolIpxFrames_Object=MibScalar
tRingStatsRingProtocolIpxFrames=_TRingStatsRingProtocolIpxFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2,5),_TRingStatsRingProtocolIpxFrames_Type())
tRingStatsRingProtocolIpxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingProtocolIpxFrames.setStatus(_A)
_TRingStatsRingProtocolNetbiosFrames_Type=Counter32
_TRingStatsRingProtocolNetbiosFrames_Object=MibScalar
tRingStatsRingProtocolNetbiosFrames=_TRingStatsRingProtocolNetbiosFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2,6),_TRingStatsRingProtocolNetbiosFrames_Type())
tRingStatsRingProtocolNetbiosFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingProtocolNetbiosFrames.setStatus(_A)
_TRingStatsRingProtocolLanNetMgrFrames_Type=Counter32
_TRingStatsRingProtocolLanNetMgrFrames_Object=MibScalar
tRingStatsRingProtocolLanNetMgrFrames=_TRingStatsRingProtocolLanNetMgrFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2,7),_TRingStatsRingProtocolLanNetMgrFrames_Type())
tRingStatsRingProtocolLanNetMgrFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingProtocolLanNetMgrFrames.setStatus(_A)
_TRingStatsRingProtocolOtherFrames_Type=Counter32
_TRingStatsRingProtocolOtherFrames_Object=MibScalar
tRingStatsRingProtocolOtherFrames=_TRingStatsRingProtocolOtherFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,2,8),_TRingStatsRingProtocolOtherFrames_Type())
tRingStatsRingProtocolOtherFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingProtocolOtherFrames.setStatus(_A)
_TRingStatsRingSizes_ObjectIdentity=ObjectIdentity
tRingStatsRingSizes=_TRingStatsRingSizes_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3))
_TRingStatsRingFramesizeUpTo63Bytes_Type=Counter32
_TRingStatsRingFramesizeUpTo63Bytes_Object=MibScalar
tRingStatsRingFramesizeUpTo63Bytes=_TRingStatsRingFramesizeUpTo63Bytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3,1),_TRingStatsRingFramesizeUpTo63Bytes_Type())
tRingStatsRingFramesizeUpTo63Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFramesizeUpTo63Bytes.setStatus(_A)
_TRingStatsRingFramesize64To127Bytes_Type=Counter32
_TRingStatsRingFramesize64To127Bytes_Object=MibScalar
tRingStatsRingFramesize64To127Bytes=_TRingStatsRingFramesize64To127Bytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3,2),_TRingStatsRingFramesize64To127Bytes_Type())
tRingStatsRingFramesize64To127Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFramesize64To127Bytes.setStatus(_A)
_TRingStatsRingFramesize128To255Bytes_Type=Counter32
_TRingStatsRingFramesize128To255Bytes_Object=MibScalar
tRingStatsRingFramesize128To255Bytes=_TRingStatsRingFramesize128To255Bytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3,3),_TRingStatsRingFramesize128To255Bytes_Type())
tRingStatsRingFramesize128To255Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFramesize128To255Bytes.setStatus(_A)
_TRingStatsRingFramesize256To511Bytes_Type=Counter32
_TRingStatsRingFramesize256To511Bytes_Object=MibScalar
tRingStatsRingFramesize256To511Bytes=_TRingStatsRingFramesize256To511Bytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3,4),_TRingStatsRingFramesize256To511Bytes_Type())
tRingStatsRingFramesize256To511Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFramesize256To511Bytes.setStatus(_A)
_TRingStatsRingFramesize512To1023Bytes_Type=Counter32
_TRingStatsRingFramesize512To1023Bytes_Object=MibScalar
tRingStatsRingFramesize512To1023Bytes=_TRingStatsRingFramesize512To1023Bytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3,5),_TRingStatsRingFramesize512To1023Bytes_Type())
tRingStatsRingFramesize512To1023Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFramesize512To1023Bytes.setStatus(_A)
_TRingStatsRingFramesize1024To2047Bytes_Type=Counter32
_TRingStatsRingFramesize1024To2047Bytes_Object=MibScalar
tRingStatsRingFramesize1024To2047Bytes=_TRingStatsRingFramesize1024To2047Bytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3,6),_TRingStatsRingFramesize1024To2047Bytes_Type())
tRingStatsRingFramesize1024To2047Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFramesize1024To2047Bytes.setStatus(_A)
_TRingStatsRingFramesize2048To4095Bytes_Type=Counter32
_TRingStatsRingFramesize2048To4095Bytes_Object=MibScalar
tRingStatsRingFramesize2048To4095Bytes=_TRingStatsRingFramesize2048To4095Bytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3,7),_TRingStatsRingFramesize2048To4095Bytes_Type())
tRingStatsRingFramesize2048To4095Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFramesize2048To4095Bytes.setStatus(_A)
_TRingStatsRingFramesize4096AndUpBytes_Type=Counter32
_TRingStatsRingFramesize4096AndUpBytes_Object=MibScalar
tRingStatsRingFramesize4096AndUpBytes=_TRingStatsRingFramesize4096AndUpBytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,1,3,8),_TRingStatsRingFramesize4096AndUpBytes_Type())
tRingStatsRingFramesize4096AndUpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsRingFramesize4096AndUpBytes.setStatus(_A)
_TRingStatsStn_ObjectIdentity=ObjectIdentity
tRingStatsStn=_TRingStatsStn_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2))
_TRingStatsStnTable_Object=MibTable
tRingStatsStnTable=_TRingStatsStnTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1))
if mibBuilder.loadTexts:tRingStatsStnTable.setStatus(_A)
_TRingStatsStnEntry_Object=MibTableRow
tRingStatsStnEntry=_TRingStatsStnEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1))
tRingStatsStnEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:tRingStatsStnEntry.setStatus(_A)
class _TRingStatsStnAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingStatsStnAddress_Type.__name__=_G
_TRingStatsStnAddress_Object=MibTableColumn
tRingStatsStnAddress=_TRingStatsStnAddress_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,1),_TRingStatsStnAddress_Type())
tRingStatsStnAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnAddress.setStatus(_A)
_TRingStatsStnFrames_Type=Counter32
_TRingStatsStnFrames_Object=MibTableColumn
tRingStatsStnFrames=_TRingStatsStnFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,2),_TRingStatsStnFrames_Type())
tRingStatsStnFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnFrames.setStatus(_A)
_TRingStatsStnBytes_Type=Counter32
_TRingStatsStnBytes_Object=MibTableColumn
tRingStatsStnBytes=_TRingStatsStnBytes_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,3),_TRingStatsStnBytes_Type())
tRingStatsStnBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnBytes.setStatus(_A)
_TRingStatsStnLineErrors_Type=Counter32
_TRingStatsStnLineErrors_Object=MibTableColumn
tRingStatsStnLineErrors=_TRingStatsStnLineErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,4),_TRingStatsStnLineErrors_Type())
tRingStatsStnLineErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnLineErrors.setStatus(_A)
_TRingStatsStnBurstErrors_Type=Counter32
_TRingStatsStnBurstErrors_Object=MibTableColumn
tRingStatsStnBurstErrors=_TRingStatsStnBurstErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,5),_TRingStatsStnBurstErrors_Type())
tRingStatsStnBurstErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnBurstErrors.setStatus(_A)
_TRingStatsStnACErrors_Type=Counter32
_TRingStatsStnACErrors_Object=MibTableColumn
tRingStatsStnACErrors=_TRingStatsStnACErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,6),_TRingStatsStnACErrors_Type())
tRingStatsStnACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnACErrors.setStatus(_A)
_TRingStatsStnAbortSequences_Type=Counter32
_TRingStatsStnAbortSequences_Object=MibTableColumn
tRingStatsStnAbortSequences=_TRingStatsStnAbortSequences_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,7),_TRingStatsStnAbortSequences_Type())
tRingStatsStnAbortSequences.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnAbortSequences.setStatus(_A)
_TRingStatsStnInternalErrors_Type=Counter32
_TRingStatsStnInternalErrors_Object=MibTableColumn
tRingStatsStnInternalErrors=_TRingStatsStnInternalErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,8),_TRingStatsStnInternalErrors_Type())
tRingStatsStnInternalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnInternalErrors.setStatus(_A)
_TRingStatsStnLostFrames_Type=Counter32
_TRingStatsStnLostFrames_Object=MibTableColumn
tRingStatsStnLostFrames=_TRingStatsStnLostFrames_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,9),_TRingStatsStnLostFrames_Type())
tRingStatsStnLostFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnLostFrames.setStatus(_A)
_TRingStatsStnCongestErrors_Type=Counter32
_TRingStatsStnCongestErrors_Object=MibTableColumn
tRingStatsStnCongestErrors=_TRingStatsStnCongestErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,10),_TRingStatsStnCongestErrors_Type())
tRingStatsStnCongestErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnCongestErrors.setStatus(_A)
_TRingStatsStnFCErrors_Type=Counter32
_TRingStatsStnFCErrors_Object=MibTableColumn
tRingStatsStnFCErrors=_TRingStatsStnFCErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,11),_TRingStatsStnFCErrors_Type())
tRingStatsStnFCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnFCErrors.setStatus(_A)
_TRingStatsStnTokenErrors_Type=Counter32
_TRingStatsStnTokenErrors_Object=MibTableColumn
tRingStatsStnTokenErrors=_TRingStatsStnTokenErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,12),_TRingStatsStnTokenErrors_Type())
tRingStatsStnTokenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnTokenErrors.setStatus(_A)
_TRingStatsStnFreqErrors_Type=Counter32
_TRingStatsStnFreqErrors_Object=MibTableColumn
tRingStatsStnFreqErrors=_TRingStatsStnFreqErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,13),_TRingStatsStnFreqErrors_Type())
tRingStatsStnFreqErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnFreqErrors.setStatus(_A)
_TRingStatsStnErrors_Type=Counter32
_TRingStatsStnErrors_Object=MibTableColumn
tRingStatsStnErrors=_TRingStatsStnErrors_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,2,1,1,14),_TRingStatsStnErrors_Type())
tRingStatsStnErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsStnErrors.setStatus(_A)
_TRingStatsReset_ObjectIdentity=ObjectIdentity
tRingStatsReset=_TRingStatsReset_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,2,3))
class _TRingStatsResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noResetCounters',1),('resetCounters',2)))
_TRingStatsResetCounters_Type.__name__=_D
_TRingStatsResetCounters_Object=MibScalar
tRingStatsResetCounters=_TRingStatsResetCounters_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,3,1),_TRingStatsResetCounters_Type())
tRingStatsResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingStatsResetCounters.setStatus(_A)
_TRingStatsResetTime_Type=TimeTicks
_TRingStatsResetTime_Object=MibScalar
tRingStatsResetTime=_TRingStatsResetTime_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,2,3,2),_TRingStatsResetTime_Type())
tRingStatsResetTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingStatsResetTime.setStatus(_A)
_TRingAlarms_ObjectIdentity=ObjectIdentity
tRingAlarms=_TRingAlarms_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,3))
_TRingAlarmsRing_ObjectIdentity=ObjectIdentity
tRingAlarmsRing=_TRingAlarmsRing_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1))
_TRingAlarmsRingEnbl_ObjectIdentity=ObjectIdentity
tRingAlarmsRingEnbl=_TRingAlarmsRingEnbl_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1))
_TRingAlarmsRingTimebase_Type=Integer32
_TRingAlarmsRingTimebase_Object=MibScalar
tRingAlarmsRingTimebase=_TRingAlarmsRingTimebase_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1,1),_TRingAlarmsRingTimebase_Type())
tRingAlarmsRingTimebase.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingTimebase.setStatus(_A)
class _TRingAlarmsRingRingPurgesEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsRingRingPurgesEnable_Type.__name__=_D
_TRingAlarmsRingRingPurgesEnable_Object=MibScalar
tRingAlarmsRingRingPurgesEnable=_TRingAlarmsRingRingPurgesEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1,2),_TRingAlarmsRingRingPurgesEnable_Type())
tRingAlarmsRingRingPurgesEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingRingPurgesEnable.setStatus(_A)
class _TRingAlarmsRingAMPErrsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsRingAMPErrsEnable_Type.__name__=_D
_TRingAlarmsRingAMPErrsEnable_Object=MibScalar
tRingAlarmsRingAMPErrsEnable=_TRingAlarmsRingAMPErrsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1,3),_TRingAlarmsRingAMPErrsEnable_Type())
tRingAlarmsRingAMPErrsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingAMPErrsEnable.setStatus(_A)
class _TRingAlarmsRingTokenErrsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsRingTokenErrsEnable_Type.__name__=_D
_TRingAlarmsRingTokenErrsEnable_Object=MibScalar
tRingAlarmsRingTokenErrsEnable=_TRingAlarmsRingTokenErrsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1,4),_TRingAlarmsRingTokenErrsEnable_Type())
tRingAlarmsRingTokenErrsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingTokenErrsEnable.setStatus(_A)
class _TRingAlarmsRingClaimTknErrsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsRingClaimTknErrsEnable_Type.__name__=_D
_TRingAlarmsRingClaimTknErrsEnable_Object=MibScalar
tRingAlarmsRingClaimTknErrsEnable=_TRingAlarmsRingClaimTknErrsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1,5),_TRingAlarmsRingClaimTknErrsEnable_Type())
tRingAlarmsRingClaimTknErrsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingClaimTknErrsEnable.setStatus(_A)
class _TRingAlarmsRingLostFramesEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsRingLostFramesEnable_Type.__name__=_D
_TRingAlarmsRingLostFramesEnable_Object=MibScalar
tRingAlarmsRingLostFramesEnable=_TRingAlarmsRingLostFramesEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1,6),_TRingAlarmsRingLostFramesEnable_Type())
tRingAlarmsRingLostFramesEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingLostFramesEnable.setStatus(_A)
class _TRingAlarmsRingBeaconStateEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsRingBeaconStateEnable_Type.__name__=_D
_TRingAlarmsRingBeaconStateEnable_Object=MibScalar
tRingAlarmsRingBeaconStateEnable=_TRingAlarmsRingBeaconStateEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1,7),_TRingAlarmsRingBeaconStateEnable_Type())
tRingAlarmsRingBeaconStateEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingBeaconStateEnable.setStatus(_A)
class _TRingAlarmsRingFrameCountEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsRingFrameCountEnable_Type.__name__=_D
_TRingAlarmsRingFrameCountEnable_Object=MibScalar
tRingAlarmsRingFrameCountEnable=_TRingAlarmsRingFrameCountEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,1,8),_TRingAlarmsRingFrameCountEnable_Type())
tRingAlarmsRingFrameCountEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingFrameCountEnable.setStatus(_A)
_TRingAlarmsRingThrsh_ObjectIdentity=ObjectIdentity
tRingAlarmsRingThrsh=_TRingAlarmsRingThrsh_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,2))
_TRingAlarmsRingRingPurgesThreshold_Type=Integer32
_TRingAlarmsRingRingPurgesThreshold_Object=MibScalar
tRingAlarmsRingRingPurgesThreshold=_TRingAlarmsRingRingPurgesThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,2,1),_TRingAlarmsRingRingPurgesThreshold_Type())
tRingAlarmsRingRingPurgesThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingRingPurgesThreshold.setStatus(_A)
_TRingAlarmsRingAMPErrsThreshold_Type=Integer32
_TRingAlarmsRingAMPErrsThreshold_Object=MibScalar
tRingAlarmsRingAMPErrsThreshold=_TRingAlarmsRingAMPErrsThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,2,2),_TRingAlarmsRingAMPErrsThreshold_Type())
tRingAlarmsRingAMPErrsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingAMPErrsThreshold.setStatus(_A)
_TRingAlarmsRingTokenErrsThreshold_Type=Integer32
_TRingAlarmsRingTokenErrsThreshold_Object=MibScalar
tRingAlarmsRingTokenErrsThreshold=_TRingAlarmsRingTokenErrsThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,2,3),_TRingAlarmsRingTokenErrsThreshold_Type())
tRingAlarmsRingTokenErrsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingTokenErrsThreshold.setStatus(_A)
_TRingAlarmsRingClaimTknThreshold_Type=Integer32
_TRingAlarmsRingClaimTknThreshold_Object=MibScalar
tRingAlarmsRingClaimTknThreshold=_TRingAlarmsRingClaimTknThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,2,4),_TRingAlarmsRingClaimTknThreshold_Type())
tRingAlarmsRingClaimTknThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingClaimTknThreshold.setStatus(_A)
_TRingAlarmsRingLostFramesThreshold_Type=Integer32
_TRingAlarmsRingLostFramesThreshold_Object=MibScalar
tRingAlarmsRingLostFramesThreshold=_TRingAlarmsRingLostFramesThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,2,5),_TRingAlarmsRingLostFramesThreshold_Type())
tRingAlarmsRingLostFramesThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingLostFramesThreshold.setStatus(_A)
_TRingAlarmsRingBeaconStateThreshold_Type=Integer32
_TRingAlarmsRingBeaconStateThreshold_Object=MibScalar
tRingAlarmsRingBeaconStateThreshold=_TRingAlarmsRingBeaconStateThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,2,6),_TRingAlarmsRingBeaconStateThreshold_Type())
tRingAlarmsRingBeaconStateThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingBeaconStateThreshold.setStatus(_A)
_TRingAlarmsRingFrameCountThreshold_Type=Integer32
_TRingAlarmsRingFrameCountThreshold_Object=MibScalar
tRingAlarmsRingFrameCountThreshold=_TRingAlarmsRingFrameCountThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,1,2,7),_TRingAlarmsRingFrameCountThreshold_Type())
tRingAlarmsRingFrameCountThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsRingFrameCountThreshold.setStatus(_A)
_TRingAlarmsStn_ObjectIdentity=ObjectIdentity
tRingAlarmsStn=_TRingAlarmsStn_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2))
_TRingAlarmsStnEnbl_ObjectIdentity=ObjectIdentity
tRingAlarmsStnEnbl=_TRingAlarmsStnEnbl_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1))
_TRingAlarmsStnEnblTable_Object=MibTable
tRingAlarmsStnEnblTable=_TRingAlarmsStnEnblTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1,1))
if mibBuilder.loadTexts:tRingAlarmsStnEnblTable.setStatus(_A)
_TRingAlarmsStnEnblEntry_Object=MibTableRow
tRingAlarmsStnEnblEntry=_TRingAlarmsStnEnblEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1,1,1))
tRingAlarmsStnEnblEntry.setIndexNames((0,_H,_S))
if mibBuilder.loadTexts:tRingAlarmsStnEnblEntry.setStatus(_A)
_TRingAlarmsStnEnblAddress_Type=OctetString
_TRingAlarmsStnEnblAddress_Object=MibTableColumn
tRingAlarmsStnEnblAddress=_TRingAlarmsStnEnblAddress_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1,1,1,1),_TRingAlarmsStnEnblAddress_Type())
tRingAlarmsStnEnblAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingAlarmsStnEnblAddress.setStatus(_A)
class _TRingAlarmsStnEnblLineErrsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsStnEnblLineErrsEnable_Type.__name__=_D
_TRingAlarmsStnEnblLineErrsEnable_Object=MibTableColumn
tRingAlarmsStnEnblLineErrsEnable=_TRingAlarmsStnEnblLineErrsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1,1,1,2),_TRingAlarmsStnEnblLineErrsEnable_Type())
tRingAlarmsStnEnblLineErrsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnEnblLineErrsEnable.setStatus(_A)
class _TRingAlarmsStnEnblInternalErrsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsStnEnblInternalErrsEnable_Type.__name__=_D
_TRingAlarmsStnEnblInternalErrsEnable_Object=MibTableColumn
tRingAlarmsStnEnblInternalErrsEnable=_TRingAlarmsStnEnblInternalErrsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1,1,1,3),_TRingAlarmsStnEnblInternalErrsEnable_Type())
tRingAlarmsStnEnblInternalErrsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnEnblInternalErrsEnable.setStatus(_A)
class _TRingAlarmsStnEnblBurstErrsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsStnEnblBurstErrsEnable_Type.__name__=_D
_TRingAlarmsStnEnblBurstErrsEnable_Object=MibTableColumn
tRingAlarmsStnEnblBurstErrsEnable=_TRingAlarmsStnEnblBurstErrsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1,1,1,4),_TRingAlarmsStnEnblBurstErrsEnable_Type())
tRingAlarmsStnEnblBurstErrsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnEnblBurstErrsEnable.setStatus(_A)
class _TRingAlarmsStnEnblACErrsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsStnEnblACErrsEnable_Type.__name__=_D
_TRingAlarmsStnEnblACErrsEnable_Object=MibTableColumn
tRingAlarmsStnEnblACErrsEnable=_TRingAlarmsStnEnblACErrsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1,1,1,5),_TRingAlarmsStnEnblACErrsEnable_Type())
tRingAlarmsStnEnblACErrsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnEnblACErrsEnable.setStatus(_A)
class _TRingAlarmsStnEnblRcvrCongestEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingAlarmsStnEnblRcvrCongestEnable_Type.__name__=_D
_TRingAlarmsStnEnblRcvrCongestEnable_Object=MibTableColumn
tRingAlarmsStnEnblRcvrCongestEnable=_TRingAlarmsStnEnblRcvrCongestEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,1,1,1,6),_TRingAlarmsStnEnblRcvrCongestEnable_Type())
tRingAlarmsStnEnblRcvrCongestEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnEnblRcvrCongestEnable.setStatus(_A)
_TRingAlarmsStnThrsh_ObjectIdentity=ObjectIdentity
tRingAlarmsStnThrsh=_TRingAlarmsStnThrsh_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2))
_TRingAlarmsStnThrshTable_Object=MibTable
tRingAlarmsStnThrshTable=_TRingAlarmsStnThrshTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2,1))
if mibBuilder.loadTexts:tRingAlarmsStnThrshTable.setStatus(_A)
_TRingAlarmsStnThrshEntry_Object=MibTableRow
tRingAlarmsStnThrshEntry=_TRingAlarmsStnThrshEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2,1,1))
tRingAlarmsStnThrshEntry.setIndexNames((0,_H,_T))
if mibBuilder.loadTexts:tRingAlarmsStnThrshEntry.setStatus(_A)
_TRingAlarmsStnThrshAddress_Type=OctetString
_TRingAlarmsStnThrshAddress_Object=MibTableColumn
tRingAlarmsStnThrshAddress=_TRingAlarmsStnThrshAddress_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2,1,1,1),_TRingAlarmsStnThrshAddress_Type())
tRingAlarmsStnThrshAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingAlarmsStnThrshAddress.setStatus(_A)
_TRingAlarmsStnThrshLineErrsThreshold_Type=Integer32
_TRingAlarmsStnThrshLineErrsThreshold_Object=MibTableColumn
tRingAlarmsStnThrshLineErrsThreshold=_TRingAlarmsStnThrshLineErrsThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2,1,1,2),_TRingAlarmsStnThrshLineErrsThreshold_Type())
tRingAlarmsStnThrshLineErrsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnThrshLineErrsThreshold.setStatus(_A)
_TRingAlarmsStnThrshInternalErrsThreshold_Type=Integer32
_TRingAlarmsStnThrshInternalErrsThreshold_Object=MibTableColumn
tRingAlarmsStnThrshInternalErrsThreshold=_TRingAlarmsStnThrshInternalErrsThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2,1,1,3),_TRingAlarmsStnThrshInternalErrsThreshold_Type())
tRingAlarmsStnThrshInternalErrsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnThrshInternalErrsThreshold.setStatus(_A)
_TRingAlarmsStnThrshBurstErrsThreshold_Type=Integer32
_TRingAlarmsStnThrshBurstErrsThreshold_Object=MibTableColumn
tRingAlarmsStnThrshBurstErrsThreshold=_TRingAlarmsStnThrshBurstErrsThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2,1,1,4),_TRingAlarmsStnThrshBurstErrsThreshold_Type())
tRingAlarmsStnThrshBurstErrsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnThrshBurstErrsThreshold.setStatus(_A)
_TRingAlarmsStnThrshACErrsThreshold_Type=Integer32
_TRingAlarmsStnThrshACErrsThreshold_Object=MibTableColumn
tRingAlarmsStnThrshACErrsThreshold=_TRingAlarmsStnThrshACErrsThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2,1,1,5),_TRingAlarmsStnThrshACErrsThreshold_Type())
tRingAlarmsStnThrshACErrsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnThrshACErrsThreshold.setStatus(_A)
_TRingAlarmsStnThrshRcvrCongestThreshold_Type=Integer32
_TRingAlarmsStnThrshRcvrCongestThreshold_Object=MibTableColumn
tRingAlarmsStnThrshRcvrCongestThreshold=_TRingAlarmsStnThrshRcvrCongestThreshold_Object((1,3,6,1,4,1,52,4,1,2,1,1,1,3,2,2,1,1,6),_TRingAlarmsStnThrshRcvrCongestThreshold_Type())
tRingAlarmsStnThrshRcvrCongestThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingAlarmsStnThrshRcvrCongestThreshold.setStatus(_A)
_TRingPortGrp_ObjectIdentity=ObjectIdentity
tRingPortGrp=_TRingPortGrp_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,2))
_TRingPortGrpTable_Object=MibTable
tRingPortGrpTable=_TRingPortGrpTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1))
if mibBuilder.loadTexts:tRingPortGrpTable.setStatus(_A)
_TRingPortGrpEntry_Object=MibTableRow
tRingPortGrpEntry=_TRingPortGrpEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1))
tRingPortGrpEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:tRingPortGrpEntry.setStatus(_A)
_TRingPortGrpId_Type=Integer32
_TRingPortGrpId_Object=MibTableColumn
tRingPortGrpId=_TRingPortGrpId_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,1),_TRingPortGrpId_Type())
tRingPortGrpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortGrpId.setStatus(_A)
class _TRingPortGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_TRingPortGrpName_Type.__name__=_I
_TRingPortGrpName_Object=MibTableColumn
tRingPortGrpName=_TRingPortGrpName_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,2),_TRingPortGrpName_Type())
tRingPortGrpName.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortGrpName.setStatus(_A)
_TRingPortGrpStnPortCount_Type=Integer32
_TRingPortGrpStnPortCount_Object=MibTableColumn
tRingPortGrpStnPortCount=_TRingPortGrpStnPortCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,3),_TRingPortGrpStnPortCount_Type())
tRingPortGrpStnPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortGrpStnPortCount.setStatus(_A)
_TRingPortGrpRingPortCount_Type=Integer32
_TRingPortGrpRingPortCount_Object=MibTableColumn
tRingPortGrpRingPortCount=_TRingPortGrpRingPortCount_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,4),_TRingPortGrpRingPortCount_Type())
tRingPortGrpRingPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortGrpRingPortCount.setStatus(_A)
class _TRingPortGrpStnPortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_E,2)))
_TRingPortGrpStnPortsEnable_Type.__name__=_D
_TRingPortGrpStnPortsEnable_Object=MibTableColumn
tRingPortGrpStnPortsEnable=_TRingPortGrpStnPortsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,5),_TRingPortGrpStnPortsEnable_Type())
tRingPortGrpStnPortsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortGrpStnPortsEnable.setStatus(_A)
class _TRingPortGrpRingPortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_E,2)))
_TRingPortGrpRingPortsEnable_Type.__name__=_D
_TRingPortGrpRingPortsEnable_Object=MibTableColumn
tRingPortGrpRingPortsEnable=_TRingPortGrpRingPortsEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,6),_TRingPortGrpRingPortsEnable_Type())
tRingPortGrpRingPortsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortGrpRingPortsEnable.setStatus(_A)
_TRingPortGrpStnPortsOn_Type=Integer32
_TRingPortGrpStnPortsOn_Object=MibTableColumn
tRingPortGrpStnPortsOn=_TRingPortGrpStnPortsOn_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,7),_TRingPortGrpStnPortsOn_Type())
tRingPortGrpStnPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortGrpStnPortsOn.setStatus(_A)
_TRingPortGrpRingPortsOn_Type=Integer32
_TRingPortGrpRingPortsOn_Object=MibTableColumn
tRingPortGrpRingPortsOn=_TRingPortGrpRingPortsOn_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,8),_TRingPortGrpRingPortsOn_Type())
tRingPortGrpRingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortGrpRingPortsOn.setStatus(_A)
class _TRingPortGrpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('managementMode',1),('autoMode',2)))
_TRingPortGrpMode_Type.__name__=_D
_TRingPortGrpMode_Object=MibTableColumn
tRingPortGrpMode=_TRingPortGrpMode_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,9),_TRingPortGrpMode_Type())
tRingPortGrpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortGrpMode.setStatus(_A)
class _TRingPortGrpSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,16)));namedValues=NamedValues(*(('fourMegaBits',4),('sixteenMegaBits',16)))
_TRingPortGrpSpeed_Type.__name__=_D
_TRingPortGrpSpeed_Object=MibTableColumn
tRingPortGrpSpeed=_TRingPortGrpSpeed_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,10),_TRingPortGrpSpeed_Type())
tRingPortGrpSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortGrpSpeed.setStatus(_A)
class _TRingPortGrpSpeedFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_TRingPortGrpSpeedFault_Type.__name__=_D
_TRingPortGrpSpeedFault_Object=MibTableColumn
tRingPortGrpSpeedFault=_TRingPortGrpSpeedFault_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,11),_TRingPortGrpSpeedFault_Type())
tRingPortGrpSpeedFault.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortGrpSpeedFault.setStatus(_A)
class _TRingPortGrpSpeedFaultLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),('fnb',2),(_W,3),(_X,4)))
_TRingPortGrpSpeedFaultLocation_Type.__name__=_D
_TRingPortGrpSpeedFaultLocation_Object=MibTableColumn
tRingPortGrpSpeedFaultLocation=_TRingPortGrpSpeedFaultLocation_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,12),_TRingPortGrpSpeedFaultLocation_Type())
tRingPortGrpSpeedFaultLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortGrpSpeedFaultLocation.setStatus(_A)
class _TRingPortGrpBypassRingPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),('off',2),('on',3),('illegal',4)))
_TRingPortGrpBypassRingPortState_Type.__name__=_D
_TRingPortGrpBypassRingPortState_Object=MibTableColumn
tRingPortGrpBypassRingPortState=_TRingPortGrpBypassRingPortState_Object((1,3,6,1,4,1,52,4,1,2,1,1,2,1,1,13),_TRingPortGrpBypassRingPortState_Type())
tRingPortGrpBypassRingPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortGrpBypassRingPortState.setStatus(_A)
_TRingPort_ObjectIdentity=ObjectIdentity
tRingPort=_TRingPort_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,3))
_TRingPortMgmt_ObjectIdentity=ObjectIdentity
tRingPortMgmt=_TRingPortMgmt_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,3,1))
_TRingPortMgmtTable_Object=MibTable
tRingPortMgmtTable=_TRingPortMgmtTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1))
if mibBuilder.loadTexts:tRingPortMgmtTable.setStatus(_A)
_TRingPortMgmtEntry_Object=MibTableRow
tRingPortMgmtEntry=_TRingPortMgmtEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1))
tRingPortMgmtEntry.setIndexNames((0,_H,_Y),(0,_H,_Z))
if mibBuilder.loadTexts:tRingPortMgmtEntry.setStatus(_A)
_TRingPortMgmtPortId_Type=Integer32
_TRingPortMgmtPortId_Object=MibTableColumn
tRingPortMgmtPortId=_TRingPortMgmtPortId_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1,1),_TRingPortMgmtPortId_Type())
tRingPortMgmtPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortMgmtPortId.setStatus(_A)
_TRingPortMgmtPortGrpId_Type=Integer32
_TRingPortMgmtPortGrpId_Object=MibTableColumn
tRingPortMgmtPortGrpId=_TRingPortMgmtPortGrpId_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1,2),_TRingPortMgmtPortGrpId_Type())
tRingPortMgmtPortGrpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortMgmtPortGrpId.setStatus(_A)
class _TRingPortMgmtPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_TRingPortMgmtPortName_Type.__name__=_I
_TRingPortMgmtPortName_Object=MibTableColumn
tRingPortMgmtPortName=_TRingPortMgmtPortName_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1,3),_TRingPortMgmtPortName_Type())
tRingPortMgmtPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortMgmtPortName.setStatus(_A)
class _TRingPortMgmtPortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TRingPortMgmtPortAdminState_Type.__name__=_D
_TRingPortMgmtPortAdminState_Object=MibTableColumn
tRingPortMgmtPortAdminState=_TRingPortMgmtPortAdminState_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1,4),_TRingPortMgmtPortAdminState_Type())
tRingPortMgmtPortAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortMgmtPortAdminState.setStatus(_A)
class _TRingPortMgmtPortOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notOperational',1),('operational',2)))
_TRingPortMgmtPortOperState_Type.__name__=_D
_TRingPortMgmtPortOperState_Object=MibTableColumn
tRingPortMgmtPortOperState=_TRingPortMgmtPortOperState_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1,5),_TRingPortMgmtPortOperState_Type())
tRingPortMgmtPortOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortMgmtPortOperState.setStatus(_A)
_TRingPortMgmtPortType_Type=ObjectIdentifier
_TRingPortMgmtPortType_Object=MibTableColumn
tRingPortMgmtPortType=_TRingPortMgmtPortType_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1,6),_TRingPortMgmtPortType_Type())
tRingPortMgmtPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortMgmtPortType.setStatus(_A)
class _TRingPortMgmtSpeedFaultDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notDetectable',1),(_K,2),(_L,3)))
_TRingPortMgmtSpeedFaultDetect_Type.__name__=_D
_TRingPortMgmtSpeedFaultDetect_Object=MibTableColumn
tRingPortMgmtSpeedFaultDetect=_TRingPortMgmtSpeedFaultDetect_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1,7),_TRingPortMgmtSpeedFaultDetect_Type())
tRingPortMgmtSpeedFaultDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortMgmtSpeedFaultDetect.setStatus(_A)
class _TRingPortMgmtRingOutEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notAvailable',1),(_F,2),(_E,3)))
_TRingPortMgmtRingOutEnable_Type.__name__=_D
_TRingPortMgmtRingOutEnable_Object=MibTableColumn
tRingPortMgmtRingOutEnable=_TRingPortMgmtRingOutEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,1,1,1,8),_TRingPortMgmtRingOutEnable_Type())
tRingPortMgmtRingOutEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortMgmtRingOutEnable.setStatus(_A)
_TRingPortStn_ObjectIdentity=ObjectIdentity
tRingPortStn=_TRingPortStn_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,3,2))
_TRingPortStnTable_Object=MibTable
tRingPortStnTable=_TRingPortStnTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1))
if mibBuilder.loadTexts:tRingPortStnTable.setStatus(_A)
_TRingPortStnEntry_Object=MibTableRow
tRingPortStnEntry=_TRingPortStnEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1,1))
tRingPortStnEntry.setIndexNames((0,_H,_a),(0,_H,_b))
if mibBuilder.loadTexts:tRingPortStnEntry.setStatus(_A)
_TRingPortStnPortId_Type=Integer32
_TRingPortStnPortId_Object=MibTableColumn
tRingPortStnPortId=_TRingPortStnPortId_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1,1,1),_TRingPortStnPortId_Type())
tRingPortStnPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortStnPortId.setStatus(_A)
_TRingPortStnPortGrpId_Type=Integer32
_TRingPortStnPortGrpId_Object=MibTableColumn
tRingPortStnPortGrpId=_TRingPortStnPortGrpId_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1,1,2),_TRingPortStnPortGrpId_Type())
tRingPortStnPortGrpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortStnPortGrpId.setStatus(_A)
class _TRingPortStnPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noLink',1),('link',2)))
_TRingPortStnPortLinkState_Type.__name__=_D
_TRingPortStnPortLinkState_Object=MibTableColumn
tRingPortStnPortLinkState=_TRingPortStnPortLinkState_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1,1,3),_TRingPortStnPortLinkState_Type())
tRingPortStnPortLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortStnPortLinkState.setStatus(_A)
_TRingPortStnPortLinkStateTime_Type=TimeTicks
_TRingPortStnPortLinkStateTime_Object=MibTableColumn
tRingPortStnPortLinkStateTime=_TRingPortStnPortLinkStateTime_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1,1,4),_TRingPortStnPortLinkStateTime_Type())
tRingPortStnPortLinkStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortStnPortLinkStateTime.setStatus(_A)
class _TRingPortStnPortMapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mappingEnabled',1),('mappingDisabled',2)))
_TRingPortStnPortMapEnable_Type.__name__=_D
_TRingPortStnPortMapEnable_Object=MibTableColumn
tRingPortStnPortMapEnable=_TRingPortStnPortMapEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1,1,5),_TRingPortStnPortMapEnable_Type())
tRingPortStnPortMapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortStnPortMapEnable.setStatus(_A)
class _TRingPortStnPortMappedMacAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TRingPortStnPortMappedMacAddr_Type.__name__=_G
_TRingPortStnPortMappedMacAddr_Object=MibTableColumn
tRingPortStnPortMappedMacAddr=_TRingPortStnPortMappedMacAddr_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1,1,6),_TRingPortStnPortMappedMacAddr_Type())
tRingPortStnPortMappedMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortStnPortMappedMacAddr.setStatus(_A)
class _TRingPortStnInsertionTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_TRingPortStnInsertionTrapEnable_Type.__name__=_D
_TRingPortStnInsertionTrapEnable_Object=MibTableColumn
tRingPortStnInsertionTrapEnable=_TRingPortStnInsertionTrapEnable_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,2,1,1,7),_TRingPortStnInsertionTrapEnable_Type())
tRingPortStnInsertionTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortStnInsertionTrapEnable.setStatus(_A)
_TRingPortRing_ObjectIdentity=ObjectIdentity
tRingPortRing=_TRingPortRing_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,3,3))
_TRingPortRingTable_Object=MibTable
tRingPortRingTable=_TRingPortRingTable_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1))
if mibBuilder.loadTexts:tRingPortRingTable.setStatus(_A)
_TRingPortRingEntry_Object=MibTableRow
tRingPortRingEntry=_TRingPortRingEntry_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1))
tRingPortRingEntry.setIndexNames((0,_H,_c),(0,_H,_d))
if mibBuilder.loadTexts:tRingPortRingEntry.setStatus(_A)
_TRingPortRingPortId_Type=Integer32
_TRingPortRingPortId_Object=MibTableColumn
tRingPortRingPortId=_TRingPortRingPortId_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1,1),_TRingPortRingPortId_Type())
tRingPortRingPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortRingPortId.setStatus(_A)
_TRingPortRingPortGrpId_Type=Integer32
_TRingPortRingPortGrpId_Object=MibTableColumn
tRingPortRingPortGrpId=_TRingPortRingPortGrpId_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1,2),_TRingPortRingPortGrpId_Type())
tRingPortRingPortGrpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortRingPortGrpId.setStatus(_A)
class _TRingPortRingPortClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAutowrap',1),('autowrap',2),('selectable',3)))
_TRingPortRingPortClass_Type.__name__=_D
_TRingPortRingPortClass_Object=MibTableColumn
tRingPortRingPortClass=_TRingPortRingPortClass_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1,3),_TRingPortRingPortClass_Type())
tRingPortRingPortClass.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortRingPortClass.setStatus(_A)
class _TRingPortRingPortMediaSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noSelection',1),('stp',2),('fiber',3)))
_TRingPortRingPortMediaSelect_Type.__name__=_D
_TRingPortRingPortMediaSelect_Object=MibTableColumn
tRingPortRingPortMediaSelect=_TRingPortRingPortMediaSelect_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1,4),_TRingPortRingPortMediaSelect_Type())
tRingPortRingPortMediaSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortRingPortMediaSelect.setStatus(_A)
class _TRingPortRingFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),(_K,2),(_L,3)))
_TRingPortRingFaultStatus_Type.__name__=_D
_TRingPortRingFaultStatus_Object=MibTableColumn
tRingPortRingFaultStatus=_TRingPortRingFaultStatus_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1,5),_TRingPortRingFaultStatus_Type())
tRingPortRingFaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortRingFaultStatus.setStatus(_A)
_TRingPortRingFaultStateTime_Type=TimeTicks
_TRingPortRingFaultStateTime_Object=MibTableColumn
tRingPortRingFaultStateTime=_TRingPortRingFaultStateTime_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1,6),_TRingPortRingFaultStateTime_Type())
tRingPortRingFaultStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortRingFaultStateTime.setStatus(_A)
class _TRingPortRingPhantomCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noPhantomAvailable',1),('activatePhantom',2),('deactivatePhantom',3)))
_TRingPortRingPhantomCurrent_Type.__name__=_D
_TRingPortRingPhantomCurrent_Object=MibTableColumn
tRingPortRingPhantomCurrent=_TRingPortRingPhantomCurrent_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1,7),_TRingPortRingPhantomCurrent_Type())
tRingPortRingPhantomCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:tRingPortRingPhantomCurrent.setStatus(_A)
class _TRingPortRingPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_TRingPortRingPortType_Type.__name__=_D
_TRingPortRingPortType_Object=MibTableColumn
tRingPortRingPortType=_TRingPortRingPortType_Object((1,3,6,1,4,1,52,4,1,2,1,1,3,3,1,1,8),_TRingPortRingPortType_Type())
tRingPortRingPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingPortRingPortType.setStatus(_A)
_TRingIf_ObjectIdentity=ObjectIdentity
tRingIf=_TRingIf_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,1,1,4))
_TRingIfIndex_Type=Integer32
_TRingIfIndex_Object=MibScalar
tRingIfIndex=_TRingIfIndex_Object((1,3,6,1,4,1,52,4,1,2,1,1,4,1),_TRingIfIndex_Type())
tRingIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tRingIfIndex.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'dot5Rev1':dot5Rev1,'tRing':tRing,'tRingMgmt':tRingMgmt,'tRingMgmtRing':tRingMgmtRing,'tRingMgmtRingName':tRingMgmtRingName,'tRingMgmtStnPortCount':tRingMgmtStnPortCount,'tRingMgmtRingPortCount':tRingMgmtRingPortCount,'tRingMgmtStnPortsEnable':tRingMgmtStnPortsEnable,'tRingMgmtRingPortsEnable':tRingMgmtRingPortsEnable,'tRingMgmtStnPortsOn':tRingMgmtStnPortsOn,'tRingMgmtRingPortsOn':tRingMgmtRingPortsOn,'tRingMgmtStations':tRingMgmtStations,'tRingMgmtRingState':tRingMgmtRingState,'tRingMgmtRingSpeed':tRingMgmtRingSpeed,'tRingMgmtActiveMonitor':tRingMgmtActiveMonitor,'tRingMgmtRingNumber':tRingMgmtRingNumber,'tRingMgmtBeaconRecovery':tRingMgmtBeaconRecovery,'tRingMgmtBcnRecRingPortRetryCount':tRingMgmtBcnRecRingPortRetryCount,'tRingMgmtBcnRecRingPortRetryDelay':tRingMgmtBcnRecRingPortRetryDelay,'tRingMgmtBcnRecStnPortRetryCount':tRingMgmtBcnRecStnPortRetryCount,'tRingMgmtBcnRecStnPortRetryDelay':tRingMgmtBcnRecStnPortRetryDelay,'tRingMgmtBcnRecBrdBypassRetryCount':tRingMgmtBcnRecBrdBypassRetryCount,'tRingMgmtBcnRecBrdBypassRetryDelay':tRingMgmtBcnRecBrdBypassRetryDelay,'tRingMgmtBcnRecBrdWrapRetryCount':tRingMgmtBcnRecBrdWrapRetryCount,'tRingMgmtBcnRecBrdWrapRetryDelay':tRingMgmtBcnRecBrdWrapRetryDelay,'tRingMgmtRingPollRecovery':tRingMgmtRingPollRecovery,'tRingMgmtStn':tRingMgmtStn,'tRingMgmtStnTable':tRingMgmtStnTable,'tRingMgmtStnEntry':tRingMgmtStnEntry,_O:tRingMgmtStnAddress,'tRingMgmtStnName':tRingMgmtStnName,'tRingMgmtStnBoard':tRingMgmtStnBoard,'tRingMgmtStnPort':tRingMgmtStnPort,'tRingMgmtStnUNA':tRingMgmtStnUNA,'tRingMgmtStnDNA':tRingMgmtStnDNA,'tRingMgmtStnPhysLocation':tRingMgmtStnPhysLocation,'tRingMgmtStnFuncClasses':tRingMgmtStnFuncClasses,'tRingMgmtStnPriority':tRingMgmtStnPriority,'tRingMgmtStnRemoveStn':tRingMgmtStnRemoveStn,'tRingMgmtHost':tRingMgmtHost,'tRingMgmtHostCommands':tRingMgmtHostCommands,'tRingMgmtHostOpenStatus':tRingMgmtHostOpenStatus,'tRingMgmtHostErrorStatus':tRingMgmtHostErrorStatus,'tRingMgmtHostAMContention':tRingMgmtHostAMContention,'tRingMgmtHostTErrorReport':tRingMgmtHostTErrorReport,'tRingMgmtHostLocalAdminMac':tRingMgmtHostLocalAdminMac,'tRingMgmtSecurity':tRingMgmtSecurity,'tRingMgmtSecurityAdminState':tRingMgmtSecurityAdminState,'tRingMgmtSecurityAddressAdd':tRingMgmtSecurityAddressAdd,'tRingMgmtSecurityAddressRemove':tRingMgmtSecurityAddressRemove,'tRingMgmtSecurityStnCount':tRingMgmtSecurityStnCount,'tRingMgmtSecurityTable':tRingMgmtSecurityTable,'tRingMgmtSecurityEntry':tRingMgmtSecurityEntry,_P:tRingMgmtSecurityIfIndex,_Q:tRingMgmtSecurityStnAddress,'tRingStats':tRingStats,'tRingStatsRing':tRingStatsRing,'tRingStatsRingErrs':tRingStatsRingErrs,'tRingStatsRingFrames':tRingStatsRingFrames,'tRingStatsRingKBytes':tRingStatsRingKBytes,'tRingStatsRingLineErrors':tRingStatsRingLineErrors,'tRingStatsRingBurstErrors':tRingStatsRingBurstErrors,'tRingStatsRingACErrors':tRingStatsRingACErrors,'tRingStatsRingAbortSequences':tRingStatsRingAbortSequences,'tRingStatsRingInternalErrors':tRingStatsRingInternalErrors,'tRingStatsRingLostFrames':tRingStatsRingLostFrames,'tRingStatsRingCongestErrors':tRingStatsRingCongestErrors,'tRingStatsRingFCErrors':tRingStatsRingFCErrors,'tRingStatsRingTokenErrors':tRingStatsRingTokenErrors,'tRingStatsRingFreqErrors':tRingStatsRingFreqErrors,'tRingStatsRingTotalErrors':tRingStatsRingTotalErrors,'tRingStatsRingAMChanges':tRingStatsRingAMChanges,'tRingStatsRingRingPurges':tRingStatsRingRingPurges,'tRingStatsRingBeaconEvents':tRingStatsRingBeaconEvents,'tRingStatsRingLongestBeacon':tRingStatsRingLongestBeacon,'tRingStatsRingLastBeacon':tRingStatsRingLastBeacon,'tRingStatsRingLastBeaconType':tRingStatsRingLastBeaconType,'tRingStatsRingPollFailureNoRecovery':tRingStatsRingPollFailureNoRecovery,'tRingStatsRingPollFailureNNIFrameCount':tRingStatsRingPollFailureNNIFrameCount,'tRingStatsRingPollFailureNNIFrameAddress':tRingStatsRingPollFailureNNIFrameAddress,'tRingStatsRingPollFailureLastNNIFrameTime':tRingStatsRingPollFailureLastNNIFrameTime,'tRingStatsRingPollFailureLastDNAAddress':tRingStatsRingPollFailureLastDNAAddress,'tRingStatsRingProtos':tRingStatsRingProtos,'tRingStatsRingProtocolSnaFrames':tRingStatsRingProtocolSnaFrames,'tRingStatsRingProtocolXnsFrames':tRingStatsRingProtocolXnsFrames,'tRingStatsRingProtocolTcpIpFrames':tRingStatsRingProtocolTcpIpFrames,'tRingStatsRingProtocolBanyanFrames':tRingStatsRingProtocolBanyanFrames,'tRingStatsRingProtocolIpxFrames':tRingStatsRingProtocolIpxFrames,'tRingStatsRingProtocolNetbiosFrames':tRingStatsRingProtocolNetbiosFrames,'tRingStatsRingProtocolLanNetMgrFrames':tRingStatsRingProtocolLanNetMgrFrames,'tRingStatsRingProtocolOtherFrames':tRingStatsRingProtocolOtherFrames,'tRingStatsRingSizes':tRingStatsRingSizes,'tRingStatsRingFramesizeUpTo63Bytes':tRingStatsRingFramesizeUpTo63Bytes,'tRingStatsRingFramesize64To127Bytes':tRingStatsRingFramesize64To127Bytes,'tRingStatsRingFramesize128To255Bytes':tRingStatsRingFramesize128To255Bytes,'tRingStatsRingFramesize256To511Bytes':tRingStatsRingFramesize256To511Bytes,'tRingStatsRingFramesize512To1023Bytes':tRingStatsRingFramesize512To1023Bytes,'tRingStatsRingFramesize1024To2047Bytes':tRingStatsRingFramesize1024To2047Bytes,'tRingStatsRingFramesize2048To4095Bytes':tRingStatsRingFramesize2048To4095Bytes,'tRingStatsRingFramesize4096AndUpBytes':tRingStatsRingFramesize4096AndUpBytes,'tRingStatsStn':tRingStatsStn,'tRingStatsStnTable':tRingStatsStnTable,'tRingStatsStnEntry':tRingStatsStnEntry,_R:tRingStatsStnAddress,'tRingStatsStnFrames':tRingStatsStnFrames,'tRingStatsStnBytes':tRingStatsStnBytes,'tRingStatsStnLineErrors':tRingStatsStnLineErrors,'tRingStatsStnBurstErrors':tRingStatsStnBurstErrors,'tRingStatsStnACErrors':tRingStatsStnACErrors,'tRingStatsStnAbortSequences':tRingStatsStnAbortSequences,'tRingStatsStnInternalErrors':tRingStatsStnInternalErrors,'tRingStatsStnLostFrames':tRingStatsStnLostFrames,'tRingStatsStnCongestErrors':tRingStatsStnCongestErrors,'tRingStatsStnFCErrors':tRingStatsStnFCErrors,'tRingStatsStnTokenErrors':tRingStatsStnTokenErrors,'tRingStatsStnFreqErrors':tRingStatsStnFreqErrors,'tRingStatsStnErrors':tRingStatsStnErrors,'tRingStatsReset':tRingStatsReset,'tRingStatsResetCounters':tRingStatsResetCounters,'tRingStatsResetTime':tRingStatsResetTime,'tRingAlarms':tRingAlarms,'tRingAlarmsRing':tRingAlarmsRing,'tRingAlarmsRingEnbl':tRingAlarmsRingEnbl,'tRingAlarmsRingTimebase':tRingAlarmsRingTimebase,'tRingAlarmsRingRingPurgesEnable':tRingAlarmsRingRingPurgesEnable,'tRingAlarmsRingAMPErrsEnable':tRingAlarmsRingAMPErrsEnable,'tRingAlarmsRingTokenErrsEnable':tRingAlarmsRingTokenErrsEnable,'tRingAlarmsRingClaimTknErrsEnable':tRingAlarmsRingClaimTknErrsEnable,'tRingAlarmsRingLostFramesEnable':tRingAlarmsRingLostFramesEnable,'tRingAlarmsRingBeaconStateEnable':tRingAlarmsRingBeaconStateEnable,'tRingAlarmsRingFrameCountEnable':tRingAlarmsRingFrameCountEnable,'tRingAlarmsRingThrsh':tRingAlarmsRingThrsh,'tRingAlarmsRingRingPurgesThreshold':tRingAlarmsRingRingPurgesThreshold,'tRingAlarmsRingAMPErrsThreshold':tRingAlarmsRingAMPErrsThreshold,'tRingAlarmsRingTokenErrsThreshold':tRingAlarmsRingTokenErrsThreshold,'tRingAlarmsRingClaimTknThreshold':tRingAlarmsRingClaimTknThreshold,'tRingAlarmsRingLostFramesThreshold':tRingAlarmsRingLostFramesThreshold,'tRingAlarmsRingBeaconStateThreshold':tRingAlarmsRingBeaconStateThreshold,'tRingAlarmsRingFrameCountThreshold':tRingAlarmsRingFrameCountThreshold,'tRingAlarmsStn':tRingAlarmsStn,'tRingAlarmsStnEnbl':tRingAlarmsStnEnbl,'tRingAlarmsStnEnblTable':tRingAlarmsStnEnblTable,'tRingAlarmsStnEnblEntry':tRingAlarmsStnEnblEntry,_S:tRingAlarmsStnEnblAddress,'tRingAlarmsStnEnblLineErrsEnable':tRingAlarmsStnEnblLineErrsEnable,'tRingAlarmsStnEnblInternalErrsEnable':tRingAlarmsStnEnblInternalErrsEnable,'tRingAlarmsStnEnblBurstErrsEnable':tRingAlarmsStnEnblBurstErrsEnable,'tRingAlarmsStnEnblACErrsEnable':tRingAlarmsStnEnblACErrsEnable,'tRingAlarmsStnEnblRcvrCongestEnable':tRingAlarmsStnEnblRcvrCongestEnable,'tRingAlarmsStnThrsh':tRingAlarmsStnThrsh,'tRingAlarmsStnThrshTable':tRingAlarmsStnThrshTable,'tRingAlarmsStnThrshEntry':tRingAlarmsStnThrshEntry,_T:tRingAlarmsStnThrshAddress,'tRingAlarmsStnThrshLineErrsThreshold':tRingAlarmsStnThrshLineErrsThreshold,'tRingAlarmsStnThrshInternalErrsThreshold':tRingAlarmsStnThrshInternalErrsThreshold,'tRingAlarmsStnThrshBurstErrsThreshold':tRingAlarmsStnThrshBurstErrsThreshold,'tRingAlarmsStnThrshACErrsThreshold':tRingAlarmsStnThrshACErrsThreshold,'tRingAlarmsStnThrshRcvrCongestThreshold':tRingAlarmsStnThrshRcvrCongestThreshold,'tRingPortGrp':tRingPortGrp,'tRingPortGrpTable':tRingPortGrpTable,'tRingPortGrpEntry':tRingPortGrpEntry,_U:tRingPortGrpId,'tRingPortGrpName':tRingPortGrpName,'tRingPortGrpStnPortCount':tRingPortGrpStnPortCount,'tRingPortGrpRingPortCount':tRingPortGrpRingPortCount,'tRingPortGrpStnPortsEnable':tRingPortGrpStnPortsEnable,'tRingPortGrpRingPortsEnable':tRingPortGrpRingPortsEnable,'tRingPortGrpStnPortsOn':tRingPortGrpStnPortsOn,'tRingPortGrpRingPortsOn':tRingPortGrpRingPortsOn,'tRingPortGrpMode':tRingPortGrpMode,'tRingPortGrpSpeed':tRingPortGrpSpeed,'tRingPortGrpSpeedFault':tRingPortGrpSpeedFault,'tRingPortGrpSpeedFaultLocation':tRingPortGrpSpeedFaultLocation,'tRingPortGrpBypassRingPortState':tRingPortGrpBypassRingPortState,'tRingPort':tRingPort,'tRingPortMgmt':tRingPortMgmt,'tRingPortMgmtTable':tRingPortMgmtTable,'tRingPortMgmtEntry':tRingPortMgmtEntry,_Y:tRingPortMgmtPortId,_Z:tRingPortMgmtPortGrpId,'tRingPortMgmtPortName':tRingPortMgmtPortName,'tRingPortMgmtPortAdminState':tRingPortMgmtPortAdminState,'tRingPortMgmtPortOperState':tRingPortMgmtPortOperState,'tRingPortMgmtPortType':tRingPortMgmtPortType,'tRingPortMgmtSpeedFaultDetect':tRingPortMgmtSpeedFaultDetect,'tRingPortMgmtRingOutEnable':tRingPortMgmtRingOutEnable,'tRingPortStn':tRingPortStn,'tRingPortStnTable':tRingPortStnTable,'tRingPortStnEntry':tRingPortStnEntry,_a:tRingPortStnPortId,_b:tRingPortStnPortGrpId,'tRingPortStnPortLinkState':tRingPortStnPortLinkState,'tRingPortStnPortLinkStateTime':tRingPortStnPortLinkStateTime,'tRingPortStnPortMapEnable':tRingPortStnPortMapEnable,'tRingPortStnPortMappedMacAddr':tRingPortStnPortMappedMacAddr,'tRingPortStnInsertionTrapEnable':tRingPortStnInsertionTrapEnable,'tRingPortRing':tRingPortRing,'tRingPortRingTable':tRingPortRingTable,'tRingPortRingEntry':tRingPortRingEntry,_c:tRingPortRingPortId,_d:tRingPortRingPortGrpId,'tRingPortRingPortClass':tRingPortRingPortClass,'tRingPortRingPortMediaSelect':tRingPortRingPortMediaSelect,'tRingPortRingFaultStatus':tRingPortRingFaultStatus,'tRingPortRingFaultStateTime':tRingPortRingFaultStateTime,'tRingPortRingPhantomCurrent':tRingPortRingPhantomCurrent,'tRingPortRingPortType':tRingPortRingPortType,'tRingIf':tRingIf,'tRingIfIndex':tRingIfIndex})