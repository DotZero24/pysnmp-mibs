_T='tptStackingNotifyMissedHeartbeatKey'
_S='tptStackingNotifyPrevStackRTI'
_R='tptStackingNotifyStackRTI'
_Q='tptStackingNotifyDeviceFaultCause'
_P='tptStackingNotifyPrevDeviceRTI'
_O='tptStackingNotifyDeviceRTI'
_N='rtinormal'
_M='rtipending'
_L='unrecoverable'
_K='recoverable'
_J='rlinferior'
_I='rebooting'
_H='unknown'
_G='tptStackingNotifyTimeStamp'
_F='tptStackingNotifyKey'
_E='tptStackingNotifyDeviceID'
_D='OctetString'
_C='read-only'
_B='TPT-STACKING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_products,=mibBuilder.importSymbols('TIPPINGPOINT-REG-MIB','tpt-products')
FaultCause,=mibBuilder.importSymbols('TPT-HIGH-AVAIL-MIB','FaultCause')
EnabledOrNot,=mibBuilder.importSymbols('TPT-PORT-CONFIG-MIB','EnabledOrNot')
tpt_tpa_eventsV2,tpt_tpa_objs,tpt_tpa_unkparams=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-eventsV2','tpt-tpa-objs','tpt-tpa-unkparams')
tpt_stack_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,20))
class DeviceRti(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,16,21,32,48,64)));namedValues=NamedValues(*((_H,0),(_I,5),(_J,16),(_K,21),(_L,32),(_M,48),(_N,64)))
class StackRti(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,48,64,80,96,112,128)));namedValues=NamedValues(*((_H,0),(_J,16),('invalid',48),(_I,64),(_K,80),(_L,96),(_M,112),(_N,128)))
_StackingStackRtiTimeStamp_Type=Unsigned32
_StackingStackRtiTimeStamp_Object=MibScalar
stackingStackRtiTimeStamp=_StackingStackRtiTimeStamp_Object((1,3,6,1,4,1,10734,3,3,2,20,1),_StackingStackRtiTimeStamp_Type())
stackingStackRtiTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:stackingStackRtiTimeStamp.setStatus(_A)
_StackingDeviceRTI_Type=DeviceRti
_StackingDeviceRTI_Object=MibScalar
stackingDeviceRTI=_StackingDeviceRTI_Object((1,3,6,1,4,1,10734,3,3,2,20,2),_StackingDeviceRTI_Type())
stackingDeviceRTI.setMaxAccess(_C)
if mibBuilder.loadTexts:stackingDeviceRTI.setStatus(_A)
_StackingPrevDeviceRTI_Type=DeviceRti
_StackingPrevDeviceRTI_Object=MibScalar
stackingPrevDeviceRTI=_StackingPrevDeviceRTI_Object((1,3,6,1,4,1,10734,3,3,2,20,3),_StackingPrevDeviceRTI_Type())
stackingPrevDeviceRTI.setMaxAccess(_C)
if mibBuilder.loadTexts:stackingPrevDeviceRTI.setStatus(_A)
_StackingDeviceFaultCause_Type=FaultCause
_StackingDeviceFaultCause_Object=MibScalar
stackingDeviceFaultCause=_StackingDeviceFaultCause_Object((1,3,6,1,4,1,10734,3,3,2,20,4),_StackingDeviceFaultCause_Type())
stackingDeviceFaultCause.setMaxAccess(_C)
if mibBuilder.loadTexts:stackingDeviceFaultCause.setStatus(_A)
_StackingStackRTI_Type=StackRti
_StackingStackRTI_Object=MibScalar
stackingStackRTI=_StackingStackRTI_Object((1,3,6,1,4,1,10734,3,3,2,20,5),_StackingStackRTI_Type())
stackingStackRTI.setMaxAccess(_C)
if mibBuilder.loadTexts:stackingStackRTI.setStatus(_A)
_StackingPrevStackRTI_Type=StackRti
_StackingPrevStackRTI_Object=MibScalar
stackingPrevStackRTI=_StackingPrevStackRTI_Object((1,3,6,1,4,1,10734,3,3,2,20,6),_StackingPrevStackRTI_Type())
stackingPrevStackRTI.setMaxAccess(_C)
if mibBuilder.loadTexts:stackingPrevStackRTI.setStatus(_A)
class _TptStackingNotifyDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptStackingNotifyDeviceID_Type.__name__=_D
_TptStackingNotifyDeviceID_Object=MibScalar
tptStackingNotifyDeviceID=_TptStackingNotifyDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,324),_TptStackingNotifyDeviceID_Type())
tptStackingNotifyDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyDeviceID.setStatus(_A)
class _TptStackingNotifyKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_TptStackingNotifyKey_Type.__name__=_D
_TptStackingNotifyKey_Object=MibScalar
tptStackingNotifyKey=_TptStackingNotifyKey_Object((1,3,6,1,4,1,10734,3,3,3,1,328),_TptStackingNotifyKey_Type())
tptStackingNotifyKey.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyKey.setStatus(_A)
_TptStackingNotifyTimeStamp_Type=Unsigned32
_TptStackingNotifyTimeStamp_Object=MibScalar
tptStackingNotifyTimeStamp=_TptStackingNotifyTimeStamp_Object((1,3,6,1,4,1,10734,3,3,3,1,332),_TptStackingNotifyTimeStamp_Type())
tptStackingNotifyTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyTimeStamp.setStatus(_A)
_TptStackingNotifyDeviceRTI_Type=DeviceRti
_TptStackingNotifyDeviceRTI_Object=MibScalar
tptStackingNotifyDeviceRTI=_TptStackingNotifyDeviceRTI_Object((1,3,6,1,4,1,10734,3,3,3,1,336),_TptStackingNotifyDeviceRTI_Type())
tptStackingNotifyDeviceRTI.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyDeviceRTI.setStatus(_A)
_TptStackingNotifyPrevDeviceRTI_Type=DeviceRti
_TptStackingNotifyPrevDeviceRTI_Object=MibScalar
tptStackingNotifyPrevDeviceRTI=_TptStackingNotifyPrevDeviceRTI_Object((1,3,6,1,4,1,10734,3,3,3,1,340),_TptStackingNotifyPrevDeviceRTI_Type())
tptStackingNotifyPrevDeviceRTI.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyPrevDeviceRTI.setStatus(_A)
_TptStackingNotifyDeviceFaultCause_Type=FaultCause
_TptStackingNotifyDeviceFaultCause_Object=MibScalar
tptStackingNotifyDeviceFaultCause=_TptStackingNotifyDeviceFaultCause_Object((1,3,6,1,4,1,10734,3,3,3,1,344),_TptStackingNotifyDeviceFaultCause_Type())
tptStackingNotifyDeviceFaultCause.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyDeviceFaultCause.setStatus(_A)
_TptStackingNotifyStackRTI_Type=StackRti
_TptStackingNotifyStackRTI_Object=MibScalar
tptStackingNotifyStackRTI=_TptStackingNotifyStackRTI_Object((1,3,6,1,4,1,10734,3,3,3,1,348),_TptStackingNotifyStackRTI_Type())
tptStackingNotifyStackRTI.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyStackRTI.setStatus(_A)
_TptStackingNotifyPrevStackRTI_Type=StackRti
_TptStackingNotifyPrevStackRTI_Object=MibScalar
tptStackingNotifyPrevStackRTI=_TptStackingNotifyPrevStackRTI_Object((1,3,6,1,4,1,10734,3,3,3,1,352),_TptStackingNotifyPrevStackRTI_Type())
tptStackingNotifyPrevStackRTI.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyPrevStackRTI.setStatus(_A)
class _TptStackingNotifyMissedHeartbeatKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_TptStackingNotifyMissedHeartbeatKey_Type.__name__=_D
_TptStackingNotifyMissedHeartbeatKey_Object=MibScalar
tptStackingNotifyMissedHeartbeatKey=_TptStackingNotifyMissedHeartbeatKey_Object((1,3,6,1,4,1,10734,3,3,3,1,356),_TptStackingNotifyMissedHeartbeatKey_Type())
tptStackingNotifyMissedHeartbeatKey.setMaxAccess(_C)
if mibBuilder.loadTexts:tptStackingNotifyMissedHeartbeatKey.setStatus(_A)
tptStackingDeviceRTINotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,70))
tptStackingDeviceRTINotify.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:tptStackingDeviceRTINotify.setStatus(_A)
tptStackingStackRTINotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,71))
tptStackingStackRTINotify.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:tptStackingStackRTINotify.setStatus(_A)
tptStackingMissedHeartbeatNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,72))
tptStackingMissedHeartbeatNotify.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_T)))
if mibBuilder.loadTexts:tptStackingMissedHeartbeatNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DeviceRti':DeviceRti,'StackRti':StackRti,'tpt-stack-objs':tpt_stack_objs,'stackingStackRtiTimeStamp':stackingStackRtiTimeStamp,'stackingDeviceRTI':stackingDeviceRTI,'stackingPrevDeviceRTI':stackingPrevDeviceRTI,'stackingDeviceFaultCause':stackingDeviceFaultCause,'stackingStackRTI':stackingStackRTI,'stackingPrevStackRTI':stackingPrevStackRTI,'tptStackingDeviceRTINotify':tptStackingDeviceRTINotify,'tptStackingStackRTINotify':tptStackingStackRTINotify,'tptStackingMissedHeartbeatNotify':tptStackingMissedHeartbeatNotify,_E:tptStackingNotifyDeviceID,_F:tptStackingNotifyKey,_G:tptStackingNotifyTimeStamp,_O:tptStackingNotifyDeviceRTI,_P:tptStackingNotifyPrevDeviceRTI,_Q:tptStackingNotifyDeviceFaultCause,_R:tptStackingNotifyStackRTI,_S:tptStackingNotifyPrevStackRTI,_T:tptStackingNotifyMissedHeartbeatKey})