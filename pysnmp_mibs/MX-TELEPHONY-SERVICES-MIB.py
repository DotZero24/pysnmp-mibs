_A9='telephonyServicesIpAddressCallVer1'
_A8='telephonyServicesUrgentGatewayVer1'
_A7='telephonyServicesCallWaitingCancelVer1'
_A6='telephonyServicesCallForwardOnNoAnswerVer1'
_A5='telephonyServicesCallForwardOnNoAnswerActivationVer1'
_A4='telephonyServicesCallForwardBusyVer1'
_A3='telephonyServicesCallForwardBusyActivationVer1'
_A2='telephonyServicesCallForwardUnconditionnalVer1'
_A1='telephonyServicesCallForwardUnconditionnalActivationVer1'
_A0='telephonyServicesAutoSpeedDialVer1'
_z='telephonyServicesActivationVer1'
_y='telephonyServicesStatusVer1'
_x='telephonyServicesIpAddressCallEnable'
_w='telephonyServicesUrgentGatewayTargetAddress'
_v='telephonyServicesUrgentGatewayDigitMap'
_u='telephonyServicesUrgentGatewayEnable'
_t='telephonyServicesCallWaitingCancelDigitMap'
_s='telephonyServicesCallWaitingCancelEnable'
_r='telephonyServicesCallForwardOnNoAnswerTimeout'
_q='telephonyServicesCallForwardOnNoAnswerDisableDigitMap'
_p='telephonyServicesCallForwardOnNoAnswerEnableDigitMap'
_o='telephonyServicesCallForwardOnNoAnswerForwardingAddress'
_n='telephonyServicesCallForwardOnNoAnswerEnable'
_m='telephonyServicesCallForwardOnNoAnswerActivation'
_l='telephonyServicesCallForwardBusyDisableDigitMap'
_k='telephonyServicesCallForwardBusyEnableDigitMap'
_j='telephonyServicesCallForwardBusyForwardingAddress'
_i='telephonyServicesCallForwardBusyEnable'
_h='telephonyServicesCallForwardBusyActivation'
_g='telephonyServicesCallForwardUnconditionnalDisableDigitMap'
_f='telephonyServicesCallForwardUnconditionnalEnableDigitMap'
_e='telephonyServicesCallForwardUnconditionnalForwardingAddress'
_d='telephonyServicesCallForwardUnconditionnalEnable'
_c='telephonyServicesCallForwardUnconditionnalActivation'
_b='telephonyServicesAutoSpeedDialTargetAddress'
_a='telephonyServicesAutoSpeedDialEnable'
_Z='telephonyServicesConferenceEnable'
_Y='telephonyServicesAttendedTransferEnable'
_X='telephonyServicesBlindTransferEnable'
_W='telephonyServicesSecondCallEnable'
_V='telephonyServicesCallWaitingEnable'
_U='telephonyServicesHoldEnable'
_T='telephonyServicesConferenceStatus'
_S='telephonyServicesAttendedTransferStatus'
_R='telephonyServicesBlindTransferStatus'
_Q='telephonyServicesSecondCallStatus'
_P='telephonyServicesCallWaitingStatus'
_O='telephonyServicesHoldStatus'
_N='Unsigned32'
_M='read-only'
_L='active'
_K='inactive'
_J='ifIndex'
_I='IF-MIB'
_H='current'
_G='enable'
_F='disable'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='MX-TELEPHONY-SERVICES-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
telephonyServicesMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,60))
if mibBuilder.loadTexts:telephonyServicesMIB.setRevisions(('1903-04-30 00:00',))
_TelephonyServicesMIBObjects_ObjectIdentity=ObjectIdentity
telephonyServicesMIBObjects=_TelephonyServicesMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1))
_TelephonyServicesIfActivationTable_Object=MibTable
telephonyServicesIfActivationTable=_TelephonyServicesIfActivationTable_Object((1,3,6,1,4,1,4935,15,60,1,10))
if mibBuilder.loadTexts:telephonyServicesIfActivationTable.setStatus(_A)
_TelephonyServicesIfActivationEntry_Object=MibTableRow
telephonyServicesIfActivationEntry=_TelephonyServicesIfActivationEntry_Object((1,3,6,1,4,1,4935,15,60,1,10,1))
telephonyServicesIfActivationEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfActivationEntry.setStatus(_A)
class _TelephonyServicesHoldEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesHoldEnable_Type.__name__=_D
_TelephonyServicesHoldEnable_Object=MibTableColumn
telephonyServicesHoldEnable=_TelephonyServicesHoldEnable_Object((1,3,6,1,4,1,4935,15,60,1,10,1,5),_TelephonyServicesHoldEnable_Type())
telephonyServicesHoldEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesHoldEnable.setStatus(_A)
class _TelephonyServicesCallWaitingEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesCallWaitingEnable_Type.__name__=_D
_TelephonyServicesCallWaitingEnable_Object=MibTableColumn
telephonyServicesCallWaitingEnable=_TelephonyServicesCallWaitingEnable_Object((1,3,6,1,4,1,4935,15,60,1,10,1,10),_TelephonyServicesCallWaitingEnable_Type())
telephonyServicesCallWaitingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallWaitingEnable.setStatus(_A)
class _TelephonyServicesSecondCallEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesSecondCallEnable_Type.__name__=_D
_TelephonyServicesSecondCallEnable_Object=MibTableColumn
telephonyServicesSecondCallEnable=_TelephonyServicesSecondCallEnable_Object((1,3,6,1,4,1,4935,15,60,1,10,1,15),_TelephonyServicesSecondCallEnable_Type())
telephonyServicesSecondCallEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesSecondCallEnable.setStatus(_A)
class _TelephonyServicesBlindTransferEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesBlindTransferEnable_Type.__name__=_D
_TelephonyServicesBlindTransferEnable_Object=MibTableColumn
telephonyServicesBlindTransferEnable=_TelephonyServicesBlindTransferEnable_Object((1,3,6,1,4,1,4935,15,60,1,10,1,20),_TelephonyServicesBlindTransferEnable_Type())
telephonyServicesBlindTransferEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesBlindTransferEnable.setStatus(_A)
class _TelephonyServicesAttendedTransferEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesAttendedTransferEnable_Type.__name__=_D
_TelephonyServicesAttendedTransferEnable_Object=MibTableColumn
telephonyServicesAttendedTransferEnable=_TelephonyServicesAttendedTransferEnable_Object((1,3,6,1,4,1,4935,15,60,1,10,1,25),_TelephonyServicesAttendedTransferEnable_Type())
telephonyServicesAttendedTransferEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesAttendedTransferEnable.setStatus(_A)
class _TelephonyServicesConferenceEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesConferenceEnable_Type.__name__=_D
_TelephonyServicesConferenceEnable_Object=MibTableColumn
telephonyServicesConferenceEnable=_TelephonyServicesConferenceEnable_Object((1,3,6,1,4,1,4935,15,60,1,10,1,30),_TelephonyServicesConferenceEnable_Type())
telephonyServicesConferenceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesConferenceEnable.setStatus(_A)
_TelephonyServicesIfStatusTable_Object=MibTable
telephonyServicesIfStatusTable=_TelephonyServicesIfStatusTable_Object((1,3,6,1,4,1,4935,15,60,1,15))
if mibBuilder.loadTexts:telephonyServicesIfStatusTable.setStatus(_A)
_TelephonyServicesIfStatusEntry_Object=MibTableRow
telephonyServicesIfStatusEntry=_TelephonyServicesIfStatusEntry_Object((1,3,6,1,4,1,4935,15,60,1,15,1))
telephonyServicesIfStatusEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfStatusEntry.setStatus(_A)
class _TelephonyServicesHoldStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesHoldStatus_Type.__name__=_D
_TelephonyServicesHoldStatus_Object=MibTableColumn
telephonyServicesHoldStatus=_TelephonyServicesHoldStatus_Object((1,3,6,1,4,1,4935,15,60,1,15,1,5),_TelephonyServicesHoldStatus_Type())
telephonyServicesHoldStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:telephonyServicesHoldStatus.setStatus(_A)
class _TelephonyServicesCallWaitingStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesCallWaitingStatus_Type.__name__=_D
_TelephonyServicesCallWaitingStatus_Object=MibTableColumn
telephonyServicesCallWaitingStatus=_TelephonyServicesCallWaitingStatus_Object((1,3,6,1,4,1,4935,15,60,1,15,1,10),_TelephonyServicesCallWaitingStatus_Type())
telephonyServicesCallWaitingStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:telephonyServicesCallWaitingStatus.setStatus(_A)
class _TelephonyServicesSecondCallStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesSecondCallStatus_Type.__name__=_D
_TelephonyServicesSecondCallStatus_Object=MibTableColumn
telephonyServicesSecondCallStatus=_TelephonyServicesSecondCallStatus_Object((1,3,6,1,4,1,4935,15,60,1,15,1,15),_TelephonyServicesSecondCallStatus_Type())
telephonyServicesSecondCallStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:telephonyServicesSecondCallStatus.setStatus(_A)
class _TelephonyServicesBlindTransferStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesBlindTransferStatus_Type.__name__=_D
_TelephonyServicesBlindTransferStatus_Object=MibTableColumn
telephonyServicesBlindTransferStatus=_TelephonyServicesBlindTransferStatus_Object((1,3,6,1,4,1,4935,15,60,1,15,1,20),_TelephonyServicesBlindTransferStatus_Type())
telephonyServicesBlindTransferStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:telephonyServicesBlindTransferStatus.setStatus(_A)
class _TelephonyServicesAttendedTransferStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesAttendedTransferStatus_Type.__name__=_D
_TelephonyServicesAttendedTransferStatus_Object=MibTableColumn
telephonyServicesAttendedTransferStatus=_TelephonyServicesAttendedTransferStatus_Object((1,3,6,1,4,1,4935,15,60,1,15,1,25),_TelephonyServicesAttendedTransferStatus_Type())
telephonyServicesAttendedTransferStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:telephonyServicesAttendedTransferStatus.setStatus(_A)
class _TelephonyServicesConferenceStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesConferenceStatus_Type.__name__=_D
_TelephonyServicesConferenceStatus_Object=MibTableColumn
telephonyServicesConferenceStatus=_TelephonyServicesConferenceStatus_Object((1,3,6,1,4,1,4935,15,60,1,15,1,30),_TelephonyServicesConferenceStatus_Type())
telephonyServicesConferenceStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:telephonyServicesConferenceStatus.setStatus(_A)
_TelephonyServicesCustomization_ObjectIdentity=ObjectIdentity
telephonyServicesCustomization=_TelephonyServicesCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20))
_TelephonyServicesAutoSpeedDial_ObjectIdentity=ObjectIdentity
telephonyServicesAutoSpeedDial=_TelephonyServicesAutoSpeedDial_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,10))
_TelephonyServicesIfAutoSpeedDialTable_Object=MibTable
telephonyServicesIfAutoSpeedDialTable=_TelephonyServicesIfAutoSpeedDialTable_Object((1,3,6,1,4,1,4935,15,60,1,20,10,10))
if mibBuilder.loadTexts:telephonyServicesIfAutoSpeedDialTable.setStatus(_A)
_TelephonyServicesIfAutoSpeedDialEntry_Object=MibTableRow
telephonyServicesIfAutoSpeedDialEntry=_TelephonyServicesIfAutoSpeedDialEntry_Object((1,3,6,1,4,1,4935,15,60,1,20,10,10,1))
telephonyServicesIfAutoSpeedDialEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfAutoSpeedDialEntry.setStatus(_A)
class _TelephonyServicesAutoSpeedDialEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesAutoSpeedDialEnable_Type.__name__=_D
_TelephonyServicesAutoSpeedDialEnable_Object=MibTableColumn
telephonyServicesAutoSpeedDialEnable=_TelephonyServicesAutoSpeedDialEnable_Object((1,3,6,1,4,1,4935,15,60,1,20,10,10,1,5),_TelephonyServicesAutoSpeedDialEnable_Type())
telephonyServicesAutoSpeedDialEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesAutoSpeedDialEnable.setStatus(_A)
class _TelephonyServicesAutoSpeedDialTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TelephonyServicesAutoSpeedDialTargetAddress_Type.__name__=_E
_TelephonyServicesAutoSpeedDialTargetAddress_Object=MibTableColumn
telephonyServicesAutoSpeedDialTargetAddress=_TelephonyServicesAutoSpeedDialTargetAddress_Object((1,3,6,1,4,1,4935,15,60,1,20,10,10,1,10),_TelephonyServicesAutoSpeedDialTargetAddress_Type())
telephonyServicesAutoSpeedDialTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesAutoSpeedDialTargetAddress.setStatus(_A)
_TelephonyServicesCallForwardCustomization_ObjectIdentity=ObjectIdentity
telephonyServicesCallForwardCustomization=_TelephonyServicesCallForwardCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,20))
_TelephonyServicesCallForwardUnconditionnal_ObjectIdentity=ObjectIdentity
telephonyServicesCallForwardUnconditionnal=_TelephonyServicesCallForwardUnconditionnal_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,20,5))
class _TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Type.__name__=_E
_TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Object=MibScalar
telephonyServicesCallForwardUnconditionnalEnableDigitMap=_TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,5),_TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Type())
telephonyServicesCallForwardUnconditionnalEnableDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardUnconditionnalEnableDigitMap.setStatus(_A)
class _TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Type.__name__=_E
_TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Object=MibScalar
telephonyServicesCallForwardUnconditionnalDisableDigitMap=_TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,10),_TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Type())
telephonyServicesCallForwardUnconditionnalDisableDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardUnconditionnalDisableDigitMap.setStatus(_A)
_TelephonyServicesIfCallForwardUnconditionnalTable_Object=MibTable
telephonyServicesIfCallForwardUnconditionnalTable=_TelephonyServicesIfCallForwardUnconditionnalTable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,15))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardUnconditionnalTable.setStatus(_A)
_TelephonyServicesIfCallForwardUnconditionnalEntry_Object=MibTableRow
telephonyServicesIfCallForwardUnconditionnalEntry=_TelephonyServicesIfCallForwardUnconditionnalEntry_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,15,1))
telephonyServicesIfCallForwardUnconditionnalEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardUnconditionnalEntry.setStatus(_A)
class _TelephonyServicesCallForwardUnconditionnalEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesCallForwardUnconditionnalEnable_Type.__name__=_D
_TelephonyServicesCallForwardUnconditionnalEnable_Object=MibTableColumn
telephonyServicesCallForwardUnconditionnalEnable=_TelephonyServicesCallForwardUnconditionnalEnable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,15,1,5),_TelephonyServicesCallForwardUnconditionnalEnable_Type())
telephonyServicesCallForwardUnconditionnalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardUnconditionnalEnable.setStatus(_A)
class _TelephonyServicesCallForwardUnconditionnalForwardingAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TelephonyServicesCallForwardUnconditionnalForwardingAddress_Type.__name__=_E
_TelephonyServicesCallForwardUnconditionnalForwardingAddress_Object=MibTableColumn
telephonyServicesCallForwardUnconditionnalForwardingAddress=_TelephonyServicesCallForwardUnconditionnalForwardingAddress_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,15,1,10),_TelephonyServicesCallForwardUnconditionnalForwardingAddress_Type())
telephonyServicesCallForwardUnconditionnalForwardingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardUnconditionnalForwardingAddress.setStatus(_A)
_TelephonyServicesIfCallForwardUnconditionnalActivationTable_Object=MibTable
telephonyServicesIfCallForwardUnconditionnalActivationTable=_TelephonyServicesIfCallForwardUnconditionnalActivationTable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,20))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardUnconditionnalActivationTable.setStatus(_A)
_TelephonyServicesIfCallForwardUnconditionnalActivationEntry_Object=MibTableRow
telephonyServicesIfCallForwardUnconditionnalActivationEntry=_TelephonyServicesIfCallForwardUnconditionnalActivationEntry_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,20,1))
telephonyServicesIfCallForwardUnconditionnalActivationEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardUnconditionnalActivationEntry.setStatus(_A)
class _TelephonyServicesCallForwardUnconditionnalActivation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesCallForwardUnconditionnalActivation_Type.__name__=_D
_TelephonyServicesCallForwardUnconditionnalActivation_Object=MibTableColumn
telephonyServicesCallForwardUnconditionnalActivation=_TelephonyServicesCallForwardUnconditionnalActivation_Object((1,3,6,1,4,1,4935,15,60,1,20,20,5,20,1,5),_TelephonyServicesCallForwardUnconditionnalActivation_Type())
telephonyServicesCallForwardUnconditionnalActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardUnconditionnalActivation.setStatus(_A)
_TelephonyServicesCallForwardBusy_ObjectIdentity=ObjectIdentity
telephonyServicesCallForwardBusy=_TelephonyServicesCallForwardBusy_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,20,10))
class _TelephonyServicesCallForwardBusyEnableDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TelephonyServicesCallForwardBusyEnableDigitMap_Type.__name__=_E
_TelephonyServicesCallForwardBusyEnableDigitMap_Object=MibScalar
telephonyServicesCallForwardBusyEnableDigitMap=_TelephonyServicesCallForwardBusyEnableDigitMap_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,5),_TelephonyServicesCallForwardBusyEnableDigitMap_Type())
telephonyServicesCallForwardBusyEnableDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardBusyEnableDigitMap.setStatus(_A)
class _TelephonyServicesCallForwardBusyDisableDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TelephonyServicesCallForwardBusyDisableDigitMap_Type.__name__=_E
_TelephonyServicesCallForwardBusyDisableDigitMap_Object=MibScalar
telephonyServicesCallForwardBusyDisableDigitMap=_TelephonyServicesCallForwardBusyDisableDigitMap_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,10),_TelephonyServicesCallForwardBusyDisableDigitMap_Type())
telephonyServicesCallForwardBusyDisableDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardBusyDisableDigitMap.setStatus(_A)
_TelephonyServicesIfCallForwardBusyTable_Object=MibTable
telephonyServicesIfCallForwardBusyTable=_TelephonyServicesIfCallForwardBusyTable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,15))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardBusyTable.setStatus(_A)
_TelephonyServicesIfCallForwardBusyEntry_Object=MibTableRow
telephonyServicesIfCallForwardBusyEntry=_TelephonyServicesIfCallForwardBusyEntry_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,15,1))
telephonyServicesIfCallForwardBusyEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardBusyEntry.setStatus(_A)
class _TelephonyServicesCallForwardBusyEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesCallForwardBusyEnable_Type.__name__=_D
_TelephonyServicesCallForwardBusyEnable_Object=MibTableColumn
telephonyServicesCallForwardBusyEnable=_TelephonyServicesCallForwardBusyEnable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,15,1,5),_TelephonyServicesCallForwardBusyEnable_Type())
telephonyServicesCallForwardBusyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardBusyEnable.setStatus(_A)
class _TelephonyServicesCallForwardBusyForwardingAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TelephonyServicesCallForwardBusyForwardingAddress_Type.__name__=_E
_TelephonyServicesCallForwardBusyForwardingAddress_Object=MibTableColumn
telephonyServicesCallForwardBusyForwardingAddress=_TelephonyServicesCallForwardBusyForwardingAddress_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,15,1,10),_TelephonyServicesCallForwardBusyForwardingAddress_Type())
telephonyServicesCallForwardBusyForwardingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardBusyForwardingAddress.setStatus(_A)
_TelephonyServicesIfCallForwardBusyActivationTable_Object=MibTable
telephonyServicesIfCallForwardBusyActivationTable=_TelephonyServicesIfCallForwardBusyActivationTable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,20))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardBusyActivationTable.setStatus(_A)
_TelephonyServicesIfCallForwardBusyActivationEntry_Object=MibTableRow
telephonyServicesIfCallForwardBusyActivationEntry=_TelephonyServicesIfCallForwardBusyActivationEntry_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,20,1))
telephonyServicesIfCallForwardBusyActivationEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardBusyActivationEntry.setStatus(_A)
class _TelephonyServicesCallForwardBusyActivation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesCallForwardBusyActivation_Type.__name__=_D
_TelephonyServicesCallForwardBusyActivation_Object=MibTableColumn
telephonyServicesCallForwardBusyActivation=_TelephonyServicesCallForwardBusyActivation_Object((1,3,6,1,4,1,4935,15,60,1,20,20,10,20,1,5),_TelephonyServicesCallForwardBusyActivation_Type())
telephonyServicesCallForwardBusyActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardBusyActivation.setStatus(_A)
_TelephonyServicesCallForwardOnNoAnswer_ObjectIdentity=ObjectIdentity
telephonyServicesCallForwardOnNoAnswer=_TelephonyServicesCallForwardOnNoAnswer_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,20,15))
class _TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Type.__name__=_E
_TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Object=MibScalar
telephonyServicesCallForwardOnNoAnswerEnableDigitMap=_TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,5),_TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Type())
telephonyServicesCallForwardOnNoAnswerEnableDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardOnNoAnswerEnableDigitMap.setStatus(_A)
class _TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Type.__name__=_E
_TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Object=MibScalar
telephonyServicesCallForwardOnNoAnswerDisableDigitMap=_TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,10),_TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Type())
telephonyServicesCallForwardOnNoAnswerDisableDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardOnNoAnswerDisableDigitMap.setStatus(_A)
_TelephonyServicesIfCallForwardOnNoAnswerTable_Object=MibTable
telephonyServicesIfCallForwardOnNoAnswerTable=_TelephonyServicesIfCallForwardOnNoAnswerTable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,15))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardOnNoAnswerTable.setStatus(_A)
_TelephonyServicesIfCallForwardOnNoAnswerEntry_Object=MibTableRow
telephonyServicesIfCallForwardOnNoAnswerEntry=_TelephonyServicesIfCallForwardOnNoAnswerEntry_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,15,1))
telephonyServicesIfCallForwardOnNoAnswerEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardOnNoAnswerEntry.setStatus(_A)
class _TelephonyServicesCallForwardOnNoAnswerEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesCallForwardOnNoAnswerEnable_Type.__name__=_D
_TelephonyServicesCallForwardOnNoAnswerEnable_Object=MibTableColumn
telephonyServicesCallForwardOnNoAnswerEnable=_TelephonyServicesCallForwardOnNoAnswerEnable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,15,1,5),_TelephonyServicesCallForwardOnNoAnswerEnable_Type())
telephonyServicesCallForwardOnNoAnswerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardOnNoAnswerEnable.setStatus(_A)
class _TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Type.__name__=_E
_TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Object=MibTableColumn
telephonyServicesCallForwardOnNoAnswerForwardingAddress=_TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,15,1,10),_TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Type())
telephonyServicesCallForwardOnNoAnswerForwardingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardOnNoAnswerForwardingAddress.setStatus(_A)
class _TelephonyServicesCallForwardOnNoAnswerTimeout_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,120000))
_TelephonyServicesCallForwardOnNoAnswerTimeout_Type.__name__=_N
_TelephonyServicesCallForwardOnNoAnswerTimeout_Object=MibTableColumn
telephonyServicesCallForwardOnNoAnswerTimeout=_TelephonyServicesCallForwardOnNoAnswerTimeout_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,15,1,15),_TelephonyServicesCallForwardOnNoAnswerTimeout_Type())
telephonyServicesCallForwardOnNoAnswerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardOnNoAnswerTimeout.setStatus(_A)
_TelephonyServicesIfCallForwardOnNoAnswerActivationTable_Object=MibTable
telephonyServicesIfCallForwardOnNoAnswerActivationTable=_TelephonyServicesIfCallForwardOnNoAnswerActivationTable_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,20))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardOnNoAnswerActivationTable.setStatus(_A)
_TelephonyServicesIfCallForwardOnNoAnswerActivationEntry_Object=MibTableRow
telephonyServicesIfCallForwardOnNoAnswerActivationEntry=_TelephonyServicesIfCallForwardOnNoAnswerActivationEntry_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,20,1))
telephonyServicesIfCallForwardOnNoAnswerActivationEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfCallForwardOnNoAnswerActivationEntry.setStatus(_A)
class _TelephonyServicesCallForwardOnNoAnswerActivation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_TelephonyServicesCallForwardOnNoAnswerActivation_Type.__name__=_D
_TelephonyServicesCallForwardOnNoAnswerActivation_Object=MibTableColumn
telephonyServicesCallForwardOnNoAnswerActivation=_TelephonyServicesCallForwardOnNoAnswerActivation_Object((1,3,6,1,4,1,4935,15,60,1,20,20,15,20,1,5),_TelephonyServicesCallForwardOnNoAnswerActivation_Type())
telephonyServicesCallForwardOnNoAnswerActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallForwardOnNoAnswerActivation.setStatus(_A)
_TelephonyServicesCallWaitingCustomization_ObjectIdentity=ObjectIdentity
telephonyServicesCallWaitingCustomization=_TelephonyServicesCallWaitingCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,30))
_TelephonyServicesCallWaitingCancel_ObjectIdentity=ObjectIdentity
telephonyServicesCallWaitingCancel=_TelephonyServicesCallWaitingCancel_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,30,5))
class _TelephonyServicesCallWaitingCancelDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TelephonyServicesCallWaitingCancelDigitMap_Type.__name__=_E
_TelephonyServicesCallWaitingCancelDigitMap_Object=MibScalar
telephonyServicesCallWaitingCancelDigitMap=_TelephonyServicesCallWaitingCancelDigitMap_Object((1,3,6,1,4,1,4935,15,60,1,20,30,5,5),_TelephonyServicesCallWaitingCancelDigitMap_Type())
telephonyServicesCallWaitingCancelDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallWaitingCancelDigitMap.setStatus(_A)
_TelephonyServicesIfCallWaitingCancelTable_Object=MibTable
telephonyServicesIfCallWaitingCancelTable=_TelephonyServicesIfCallWaitingCancelTable_Object((1,3,6,1,4,1,4935,15,60,1,20,30,5,10))
if mibBuilder.loadTexts:telephonyServicesIfCallWaitingCancelTable.setStatus(_A)
_TelephonyServicesIfCallWaitingCancelEntry_Object=MibTableRow
telephonyServicesIfCallWaitingCancelEntry=_TelephonyServicesIfCallWaitingCancelEntry_Object((1,3,6,1,4,1,4935,15,60,1,20,30,5,10,1))
telephonyServicesIfCallWaitingCancelEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:telephonyServicesIfCallWaitingCancelEntry.setStatus(_A)
class _TelephonyServicesCallWaitingCancelEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesCallWaitingCancelEnable_Type.__name__=_D
_TelephonyServicesCallWaitingCancelEnable_Object=MibTableColumn
telephonyServicesCallWaitingCancelEnable=_TelephonyServicesCallWaitingCancelEnable_Object((1,3,6,1,4,1,4935,15,60,1,20,30,5,10,1,5),_TelephonyServicesCallWaitingCancelEnable_Type())
telephonyServicesCallWaitingCancelEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesCallWaitingCancelEnable.setStatus(_A)
_TelephonyServicesUrgentGatewayCustomization_ObjectIdentity=ObjectIdentity
telephonyServicesUrgentGatewayCustomization=_TelephonyServicesUrgentGatewayCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,35))
class _TelephonyServicesUrgentGatewayEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesUrgentGatewayEnable_Type.__name__=_D
_TelephonyServicesUrgentGatewayEnable_Object=MibScalar
telephonyServicesUrgentGatewayEnable=_TelephonyServicesUrgentGatewayEnable_Object((1,3,6,1,4,1,4935,15,60,1,20,35,5),_TelephonyServicesUrgentGatewayEnable_Type())
telephonyServicesUrgentGatewayEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesUrgentGatewayEnable.setStatus(_A)
class _TelephonyServicesUrgentGatewayDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TelephonyServicesUrgentGatewayDigitMap_Type.__name__=_E
_TelephonyServicesUrgentGatewayDigitMap_Object=MibScalar
telephonyServicesUrgentGatewayDigitMap=_TelephonyServicesUrgentGatewayDigitMap_Object((1,3,6,1,4,1,4935,15,60,1,20,35,10),_TelephonyServicesUrgentGatewayDigitMap_Type())
telephonyServicesUrgentGatewayDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesUrgentGatewayDigitMap.setStatus(_A)
class _TelephonyServicesUrgentGatewayTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TelephonyServicesUrgentGatewayTargetAddress_Type.__name__=_E
_TelephonyServicesUrgentGatewayTargetAddress_Object=MibScalar
telephonyServicesUrgentGatewayTargetAddress=_TelephonyServicesUrgentGatewayTargetAddress_Object((1,3,6,1,4,1,4935,15,60,1,20,35,15),_TelephonyServicesUrgentGatewayTargetAddress_Type())
telephonyServicesUrgentGatewayTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesUrgentGatewayTargetAddress.setStatus(_A)
_TelephonyServicesIpAddressCallCustomization_ObjectIdentity=ObjectIdentity
telephonyServicesIpAddressCallCustomization=_TelephonyServicesIpAddressCallCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,60,1,20,99))
class _TelephonyServicesIpAddressCallEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TelephonyServicesIpAddressCallEnable_Type.__name__=_D
_TelephonyServicesIpAddressCallEnable_Object=MibScalar
telephonyServicesIpAddressCallEnable=_TelephonyServicesIpAddressCallEnable_Object((1,3,6,1,4,1,4935,15,60,1,20,99,5),_TelephonyServicesIpAddressCallEnable_Type())
telephonyServicesIpAddressCallEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyServicesIpAddressCallEnable.setStatus(_A)
_TelephonyServicesConformance_ObjectIdentity=ObjectIdentity
telephonyServicesConformance=_TelephonyServicesConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,60,2))
_TelephonyServicesCompliances_ObjectIdentity=ObjectIdentity
telephonyServicesCompliances=_TelephonyServicesCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,60,2,1))
_TelephonyServicesGroups_ObjectIdentity=ObjectIdentity
telephonyServicesGroups=_TelephonyServicesGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,60,2,5))
telephonyServicesStatusVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,3))
telephonyServicesStatusVer1.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:telephonyServicesStatusVer1.setStatus(_H)
telephonyServicesActivationVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,5))
telephonyServicesActivationVer1.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:telephonyServicesActivationVer1.setStatus(_H)
telephonyServicesAutoSpeedDialVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,10))
telephonyServicesAutoSpeedDialVer1.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:telephonyServicesAutoSpeedDialVer1.setStatus(_H)
telephonyServicesCallForwardUnconditionnalActivationVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,12))
telephonyServicesCallForwardUnconditionnalActivationVer1.setObjects((_B,_c))
if mibBuilder.loadTexts:telephonyServicesCallForwardUnconditionnalActivationVer1.setStatus(_H)
telephonyServicesCallForwardUnconditionnalVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,15))
telephonyServicesCallForwardUnconditionnalVer1.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:telephonyServicesCallForwardUnconditionnalVer1.setStatus(_H)
telephonyServicesCallForwardBusyActivationVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,17))
telephonyServicesCallForwardBusyActivationVer1.setObjects((_B,_h))
if mibBuilder.loadTexts:telephonyServicesCallForwardBusyActivationVer1.setStatus(_H)
telephonyServicesCallForwardBusyVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,20))
telephonyServicesCallForwardBusyVer1.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:telephonyServicesCallForwardBusyVer1.setStatus(_H)
telephonyServicesCallForwardOnNoAnswerActivationVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,22))
telephonyServicesCallForwardOnNoAnswerActivationVer1.setObjects((_B,_m))
if mibBuilder.loadTexts:telephonyServicesCallForwardOnNoAnswerActivationVer1.setStatus(_H)
telephonyServicesCallForwardOnNoAnswerVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,25))
telephonyServicesCallForwardOnNoAnswerVer1.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:telephonyServicesCallForwardOnNoAnswerVer1.setStatus(_H)
telephonyServicesCallWaitingCancelVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,30))
telephonyServicesCallWaitingCancelVer1.setObjects(*((_B,_s),(_B,_t)))
if mibBuilder.loadTexts:telephonyServicesCallWaitingCancelVer1.setStatus(_H)
telephonyServicesUrgentGatewayVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,35))
telephonyServicesUrgentGatewayVer1.setObjects(*((_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:telephonyServicesUrgentGatewayVer1.setStatus(_H)
telephonyServicesIpAddressCallVer1=ObjectGroup((1,3,6,1,4,1,4935,15,60,2,5,99))
telephonyServicesIpAddressCallVer1.setObjects((_B,_x))
if mibBuilder.loadTexts:telephonyServicesIpAddressCallVer1.setStatus(_H)
telephonyServicesComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,60,2,1,1))
telephonyServicesComplVer1.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:telephonyServicesComplVer1.setStatus(_H)
mibBuilder.exportSymbols(_B,**{'telephonyServicesMIB':telephonyServicesMIB,'telephonyServicesMIBObjects':telephonyServicesMIBObjects,'telephonyServicesIfActivationTable':telephonyServicesIfActivationTable,'telephonyServicesIfActivationEntry':telephonyServicesIfActivationEntry,_U:telephonyServicesHoldEnable,_V:telephonyServicesCallWaitingEnable,_W:telephonyServicesSecondCallEnable,_X:telephonyServicesBlindTransferEnable,_Y:telephonyServicesAttendedTransferEnable,_Z:telephonyServicesConferenceEnable,'telephonyServicesIfStatusTable':telephonyServicesIfStatusTable,'telephonyServicesIfStatusEntry':telephonyServicesIfStatusEntry,_O:telephonyServicesHoldStatus,_P:telephonyServicesCallWaitingStatus,_Q:telephonyServicesSecondCallStatus,_R:telephonyServicesBlindTransferStatus,_S:telephonyServicesAttendedTransferStatus,_T:telephonyServicesConferenceStatus,'telephonyServicesCustomization':telephonyServicesCustomization,'telephonyServicesAutoSpeedDial':telephonyServicesAutoSpeedDial,'telephonyServicesIfAutoSpeedDialTable':telephonyServicesIfAutoSpeedDialTable,'telephonyServicesIfAutoSpeedDialEntry':telephonyServicesIfAutoSpeedDialEntry,_a:telephonyServicesAutoSpeedDialEnable,_b:telephonyServicesAutoSpeedDialTargetAddress,'telephonyServicesCallForwardCustomization':telephonyServicesCallForwardCustomization,'telephonyServicesCallForwardUnconditionnal':telephonyServicesCallForwardUnconditionnal,_f:telephonyServicesCallForwardUnconditionnalEnableDigitMap,_g:telephonyServicesCallForwardUnconditionnalDisableDigitMap,'telephonyServicesIfCallForwardUnconditionnalTable':telephonyServicesIfCallForwardUnconditionnalTable,'telephonyServicesIfCallForwardUnconditionnalEntry':telephonyServicesIfCallForwardUnconditionnalEntry,_d:telephonyServicesCallForwardUnconditionnalEnable,_e:telephonyServicesCallForwardUnconditionnalForwardingAddress,'telephonyServicesIfCallForwardUnconditionnalActivationTable':telephonyServicesIfCallForwardUnconditionnalActivationTable,'telephonyServicesIfCallForwardUnconditionnalActivationEntry':telephonyServicesIfCallForwardUnconditionnalActivationEntry,_c:telephonyServicesCallForwardUnconditionnalActivation,'telephonyServicesCallForwardBusy':telephonyServicesCallForwardBusy,_k:telephonyServicesCallForwardBusyEnableDigitMap,_l:telephonyServicesCallForwardBusyDisableDigitMap,'telephonyServicesIfCallForwardBusyTable':telephonyServicesIfCallForwardBusyTable,'telephonyServicesIfCallForwardBusyEntry':telephonyServicesIfCallForwardBusyEntry,_i:telephonyServicesCallForwardBusyEnable,_j:telephonyServicesCallForwardBusyForwardingAddress,'telephonyServicesIfCallForwardBusyActivationTable':telephonyServicesIfCallForwardBusyActivationTable,'telephonyServicesIfCallForwardBusyActivationEntry':telephonyServicesIfCallForwardBusyActivationEntry,_h:telephonyServicesCallForwardBusyActivation,'telephonyServicesCallForwardOnNoAnswer':telephonyServicesCallForwardOnNoAnswer,_p:telephonyServicesCallForwardOnNoAnswerEnableDigitMap,_q:telephonyServicesCallForwardOnNoAnswerDisableDigitMap,'telephonyServicesIfCallForwardOnNoAnswerTable':telephonyServicesIfCallForwardOnNoAnswerTable,'telephonyServicesIfCallForwardOnNoAnswerEntry':telephonyServicesIfCallForwardOnNoAnswerEntry,_n:telephonyServicesCallForwardOnNoAnswerEnable,_o:telephonyServicesCallForwardOnNoAnswerForwardingAddress,_r:telephonyServicesCallForwardOnNoAnswerTimeout,'telephonyServicesIfCallForwardOnNoAnswerActivationTable':telephonyServicesIfCallForwardOnNoAnswerActivationTable,'telephonyServicesIfCallForwardOnNoAnswerActivationEntry':telephonyServicesIfCallForwardOnNoAnswerActivationEntry,_m:telephonyServicesCallForwardOnNoAnswerActivation,'telephonyServicesCallWaitingCustomization':telephonyServicesCallWaitingCustomization,'telephonyServicesCallWaitingCancel':telephonyServicesCallWaitingCancel,_t:telephonyServicesCallWaitingCancelDigitMap,'telephonyServicesIfCallWaitingCancelTable':telephonyServicesIfCallWaitingCancelTable,'telephonyServicesIfCallWaitingCancelEntry':telephonyServicesIfCallWaitingCancelEntry,_s:telephonyServicesCallWaitingCancelEnable,'telephonyServicesUrgentGatewayCustomization':telephonyServicesUrgentGatewayCustomization,_u:telephonyServicesUrgentGatewayEnable,_v:telephonyServicesUrgentGatewayDigitMap,_w:telephonyServicesUrgentGatewayTargetAddress,'telephonyServicesIpAddressCallCustomization':telephonyServicesIpAddressCallCustomization,_x:telephonyServicesIpAddressCallEnable,'telephonyServicesConformance':telephonyServicesConformance,'telephonyServicesCompliances':telephonyServicesCompliances,'telephonyServicesComplVer1':telephonyServicesComplVer1,'telephonyServicesGroups':telephonyServicesGroups,_y:telephonyServicesStatusVer1,_z:telephonyServicesActivationVer1,_A0:telephonyServicesAutoSpeedDialVer1,_A1:telephonyServicesCallForwardUnconditionnalActivationVer1,_A2:telephonyServicesCallForwardUnconditionnalVer1,_A3:telephonyServicesCallForwardBusyActivationVer1,_A4:telephonyServicesCallForwardBusyVer1,_A5:telephonyServicesCallForwardOnNoAnswerActivationVer1,_A6:telephonyServicesCallForwardOnNoAnswerVer1,_A7:telephonyServicesCallWaitingCancelVer1,_A8:telephonyServicesUrgentGatewayVer1,_A9:telephonyServicesIpAddressCallVer1})